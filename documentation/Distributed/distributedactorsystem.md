# DistributedActorSystem

**Framework**: Distributed  
**Kind**: protocol

A distributed actor system underpins and implements all functionality of distributed actors.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol DistributedActorSystem<SerializationRequirement> : Sendable
```

#### Overview

A [`DistributedActor`](distributedactor.md) is always initialized in association with some concrete actor system. That actor system instance is then used to manage the identity of the actor, as well as handle all remote interactions of the distributed actor.

#### Using a Distributedactorsystem Library

From a library user’s perspective (e.g. someone using a `ClusterSystem` or `SampleWebSocketActorSystem`), the basic use of a distributed actor system is fairly opaque.

Any distributed actor must declare what actor system it is able to operate with. This is done either by a `typealias ActorSystem` in the body of such `distributed actor` declaration, or a module-wide global `typealias DefaultDistributedActorSystem`. Refer to the [`DistributedActor`](distributedactor.md) documentation to learn more about the tradeoffs of these approaches.

Once an actor has declared the system it is able to work with, an instance of the system must be provided at initialization time, in order for the system to be able to take over the actor’s identity management.

For example, a simple distributed actor may look like this:

```swift
distributed actor Greeter {
  init(name: String, actorSystem: ActorSystem) {
    self.name = name
    self.actorSystem = actorSystem // required (!) initialization of implicit actorSystem property
  }
}
```

Notice that every distributed actor initializer must initialize the synthesized [`actorSystem`](distributedactor/actorsystem-swift.property.md). This property is later used for identity management and other remote interactions of the actor. For more details refer to [`DistributedActor`](distributedactor.md) which explains more about declaring distributed actors.

For more details about how the specific actor system implementation deals with remote message transports and serialization, please refer to the specific system’s documentation.

> **Note**: For example, you may refer to the [`Swift Distributed Actors cluster library`](https://developer.apple.comhttps://github.com/apple/swift-distributed-actors/) documentation, which is one example of such feature complete distributed actor system implementation.

#### Implementing a Distributedactorsystem

This section is dedicated to distributed actor system library authors, and generally can be skipped over by library users, as it explains the interactions of synthesized code and specific distributed actor system methods and how they must be implemented.

Methods discussed in this section are generally not intended to be called directly, but instead will have calls generated to them from distributed actor declarations in appropriate places (such as initializers, `distributed func` calls, or `distributed` computed properties).

##### Assigning and Resigning Actor Identifiers

During a local distributed actor’s initialization (i.e. any `init` of a `distributed actor`), the actor system will be invoked in order to assign an [`ActorID`](distributedactorsystem/actorid.md) for this actor.

A call to [`assignID(_:)`](distributedactorsystem/assignid(_:).md) is made during the initialization of the distributed actor. The snippet below showcases this, though no guarantees are made at this point about the exact placement of this call.

```swift
distributed actor ShowcaseIDInit {
  // let actorSystem: ActorSystem // synthesized;

  // typealias ID = ActorSystem.ActorID
  // let id: ID // synthesized; implements `Identifiable.id` requirement

  init(actorSystem: ActorSystem) {
    self.actorSystem = actorSystem
    // ...
    // self.id = actorSystem.assignID(Self.self) // synthesized;
    // ...
  }
}
```

The result of [`assignID(_:)`](distributedactorsystem/assignid(_:).md) is then directly stored in the synthesized `id` property of the actor.

The actor system should assign  identifiers to types, such that they may be properly resolved from any process in the distributed actor system. The exact shape of the [`ActorID`](distributedactorsystem/actorid.md) is left up to the library to decide. It can be as small as an integer based identifier, or as large as a series of key-value pairs identifying the actor.

The actor system must retain a mapping from the [`ActorID`](distributedactorsystem/actorid.md) to the specific actor  which it is given in [`actorReady(_:)`](distributedactorsystem/actorready(_:).md) in order to implement the `resolve(id:using:)` method, which is how incoming and outgoing remote calls are made possible.

Users have no control over this assignment, nor are they allowed to set the `id` property explicitly. The [`id`](distributedactor/id.md) is used to implement the distributed actor’s `Hashable`, `Equatable`, and even `Codable` conformance (which is synthesized if and only if the [`ActorID`](distributedactorsystem/actorid.md) is `Codable` itself).

> 💡 **Tip**: Take note that throwing or failable initializers complicate this somewhat. Thankfully, the compiler will always emit the right code such that every [`assignID(_:)`](distributedactorsystem/assignid(_:).md) is balanced with a [`resignID(_:)`](distributedactorsystem/resignid(_:).md) call, when the actor either failed to initialize or deinitialize properly. It is also possible that a throwing initializer throws before assigning the `actorSystem` and `id` properties. In such case, no `assignID` nor `resignID` calls are made. There is no risk of the compiler ever attempting to call a `resignID(_:)` without first having assigned given ID.

Manually invoking `assignID` and `resignID` is generally not recommended but isn’t strictly a programmer error, and it is up to the actor system to decide how to deal with such calls.

Once the `distributed actor` deinitializes, a call to [`resignID(_:)`](distributedactorsystem/resignid(_:).md) will be made. Generally this is made from the distributed actor’s `deinit`, however in the case of throwing initializers it may also happen during such failed init, in order to release the ID that is no longer used.

```swift
// Synthesized inside a distributed actor's deinit:
deinit {
  // actorSystem.resignID(self.id)
}
```

After an ID is resigned, it technically could be used to identify another instance. For example, an advanced actor system implementation could use such approach to implement actors which are created “ad-hoc” and always contain the appropriate ID, and if one isn’t allocated yet for such ID, it could  create one on demand and make sure it is assigned the required ID.

##### Readying Distributed Actors

Once a `distributed actor` has been  during its initializer, a call to [`actorReady(_:)`](distributedactorsystem/actorready(_:).md) is synthesized. This call is made after the actor’s properties (including all user-declared properties) have been initialized, but before other user-defined code in the initializer gets a chance to run.

> **Note**: Generally due to actor initializer isolation rules, users will need to make their initializers `async` in order to write code that safely performs extra actions after it has fully initialized.

The `actorReady(_)` call on the actor system is a signal to the actor system that this actor  is now ready and may be resolved and interacted with via the actor system. Generally, a distributed actor system implementation will  the actors it has readied, because retaining them strongly would mean that they will never be deallocated (and thus never resign their ID’s).

> **Note**: Generally actor systems should retain actors  in order to allow them be deinitialized when no longer in use. Sometimes though, it can be quite useful to have the system retain certain “well known” actors, for example when it is expected that other nodes in the distributed system will need to interact with them, even if end-user code no longer holds strong references to them. An example of such “retain while actor system is active” distributed actors would be any kind of actor which implements discovery or health check mechanisms between clustered nodes, sometimes called “system actors”, i.e. actors that serve the actor system directly.

Next, we will discuss the just mentioned `resolve` method, which is closely tied to readying actors.

##### Resolving Potentially Remote Distributed Actors

An important aspect of any distributed actor system is being able to turn a [`DistributedActor`](distributedactor.md) type and [`ActorID`](distributedactorsystem/actorid.md) into a reference to an actor (instance), regardless where the actor is located. The ID should have enough information stored to be able to make the decision of  the actor is located, without having to contact remote nodes. Specifically, the implementation of [`resolve(id:as:)`](distributedactorsystem/resolve(id:as:).md) is  `async` and should  perform long running or blocking operations in order to return.

> **Note**: Currently only concrete distributed actors types can be resolved.

The actor system’s [`resolve(id:as:)`](distributedactorsystem/resolve(id:as:).md) method is called by the compiler whenever end-users call the [`DistributedActor`](distributedactor.md)‘s [`resolve(id:using:)`](distributedactor/resolve(id:using:).md) method. The return types of those methods differ, as the actor system’s return type is `Act?` (and it may throw if unable to resolve the `ActorID`).

The actor system’s `resolve` returning `nil` means that the [`ActorID`](distributedactorsystem/actorid.md) passed to it refers to a  distributed actor. The Swift runtime reacts to this by creating a remote actor reference (sometimes called a “proxy”).

##### Handling Remote Calls

Finally, calls on a  distributed actor reference’s distributed methods are turned into invocations of `remoteCall(on:target:invocation:returning:throwing:)` (or `remoteCallVoid(on:target:invocation:throwing:)` for Void returning methods).

Implementing the remote calls correctly and efficiently is the important task for a distributed actor system library.

Implementations of remote calls generally will serialize `actor.id`, `target` and `invocation` into some form of wire envelope, and send it over the network (or process boundary) using some transport mechanism of their choice. As they do so, they need to suspend the `remoteCall` function, and resume it once a reply to the call arrives. Unless the transport layer is also async/await aware, this will often require making use of a `CheckedContinuation`.

While implementing remote calls please keep in mind any potential failure scenarios that may occur, such as message loss, connection failures and similar issues. Such situations should all be surfaced by resuming the `remoteCall` by throwing an error conforming to [`DistributedActorSystemError`](distributedactorsystemerror.md).

While it is not  to conform error thrown out of these methods to [`DistributedActorSystemError`](distributedactorsystemerror.md), the general guideline about conforming errors to this protocol is that errors which are outside of the user’s control, but are thrown because transport or actor system issues, should conform to it. This is to simplify separating “business logic errors” from transport errors.

##### Further Reading

For an even more in-depth explanation about the inner workings of a distributed actor system, you can refer to the following Swift Evolution proposals:

- [`SE-0336: Distributed Actor Isolation`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0336-distributed-actor-isolation.md)
- [`SE-0344: Distributed Actor Runtime`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0344-distributed-actor-runtime.md)

## Topics

### Associated Types
- [associatedtype ActorID : Hashable, Sendable](distributedactorsystem/actorid.md)
  The type ID that will be assigned to any distributed actor managed by this actor system.
- [associatedtype InvocationDecoder : DistributedTargetInvocationDecoder](distributedactorsystem/invocationdecoder.md)
  Type of [`DistributedTargetInvocationDecoder`](distributedtargetinvocationdecoder.md) that should be used when decoding invocations during [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md) calls.
- [associatedtype InvocationEncoder : DistributedTargetInvocationEncoder](distributedactorsystem/invocationencoder.md)
  Type of [`DistributedTargetInvocationEncoder`](distributedtargetinvocationencoder.md) that should be used when the Swift runtime needs to encode a distributed target call into an encoder, before passing it off to `remoteCall(...)`.
- [associatedtype ResultHandler : DistributedTargetInvocationResultHandler](distributedactorsystem/resulthandler.md)
  The type of the result handler which will be offered the results returned by a distributed function invocation called via [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md).
- [associatedtype SerializationRequirement](distributedactorsystem/serializationrequirement.md)
  The serialization requirement that will be applied to all distributed targets used with this system.
### Instance Methods
- [func actorReady<Act>(Act)](distributedactorsystem/actorready(_:).md)
  Invoked during a distributed actor’s initialization, as soon as it becomes fully initialized.
- [func assignID<Act>(Act.Type) -> Self.ActorID](distributedactorsystem/assignid(_:).md)
  Assign an [`ActorID`](distributedactorsystem/actorid.md) for the passed actor type.
- [func executeDistributedTarget<Act>(on: Act, target: RemoteCallTarget, invocationDecoder: inout Self.InvocationDecoder, handler: Self.ResultHandler) async throws](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md)
  Prepare and execute a call to the distributed function identified by the passed arguments, on the passed `actor`, and collect its results using the `ResultHandler`.
- [func invokeHandlerOnReturn(handler: Self.ResultHandler, resultBuffer: UnsafeRawPointer, metatype: any Any.Type) async throws](distributedactorsystem/invokehandleronreturn(handler:resultbuffer:metatype:).md)
  Implementation synthesized by the compiler. Not intended to be invoked explicitly from user code!
- [func makeInvocationEncoder() -> Self.InvocationEncoder](distributedactorsystem/makeinvocationencoder.md)
  Invoked by the Swift runtime when a distributed remote call is about to be made.
- [func remoteCall<Act, Err, Res>(on: Act, target: RemoteCallTarget, invocation: inout Self.InvocationEncoder, throwing: Err.Type, returning: Res.Type) async throws -> Res](distributedactorsystem/remotecall(on:target:invocation:throwing:returning:).md)
  Invoked by the Swift runtime when making a remote call.
- [func remoteCallVoid<Act, Err>(on: Act, target: RemoteCallTarget, invocation: inout Self.InvocationEncoder, throwing: Err.Type) async throws](distributedactorsystem/remotecallvoid(on:target:invocation:throwing:).md)
  Invoked by the Swift runtime when making a remote call.
- [func resignID(Self.ActorID)](distributedactorsystem/resignid(_:).md)
  Called during when a distributed actor is deinitialized, or fails to initialize completely (e.g. by throwing out of an `init` that did not completely initialize all of the actors stored properties yet).
- [func resolve<Act>(id: Self.ActorID, as: Act.Type) throws -> Act?](distributedactorsystem/resolve(id:as:).md)
  Resolves a local or remote [`ActorID`](distributedactorsystem/actorid.md) to a reference to given actor, or throws if unable to.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md)

## See Also

- [protocol DistributedActor](distributedactor.md)
  Common protocol to which all distributed actors conform implicitly.
- [macro Resolvable()](resolvable().md)
  Enables the attached to protocol to be resolved as remote distributed actor reference.
- [func buildDefaultDistributedRemoteActorExecutor<Act>(Act) -> UnownedSerialExecutor](builddefaultdistributedremoteactorexecutor(_:).md)
  Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references. The executor is shared between all remote default executor remote distributed actors, and it will crash if any job is enqueued on it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem)*