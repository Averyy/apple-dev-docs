# LocalTestingDistributedActorSystem

**Framework**: Distributed  
**Kind**: class

A `DistributedActorSystem` designed for local only testing.

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
final class LocalTestingDistributedActorSystem
```

#### Overview

It will crash on any attempt of remote communication, but can be useful for learning about `distributed actor` isolation, as well as early prototyping stages of development where a real system is not necessary yet.

## Topics

### Initializers
- [init()](localtestingdistributedactorsystem/init.md)
### Instance Methods
- [func actorReady<Act>(Act)](localtestingdistributedactorsystem/actorready(_:).md)
  Invoked during a distributed actor’s initialization, as soon as it becomes fully initialized.
- [func assignID<Act>(Act.Type) -> LocalTestingDistributedActorSystem.ActorID](localtestingdistributedactorsystem/assignid(_:).md)
  Assign an [`LocalTestingDistributedActorSystem.ActorID`](localtestingdistributedactorsystem/actorid.md) for the passed actor type.
- [func invokeHandlerOnReturn(handler: LocalTestingDistributedActorSystem.ResultHandler, resultBuffer: UnsafeRawPointer, metatype: any Any.Type) async throws](localtestingdistributedactorsystem/invokehandleronreturn(handler:resultbuffer:metatype:).md)
  Implementation synthesized by the compiler. Not intended to be invoked explicitly from user code!
- [func makeInvocationEncoder() -> LocalTestingDistributedActorSystem.InvocationEncoder](localtestingdistributedactorsystem/makeinvocationencoder.md)
  Invoked by the Swift runtime when a distributed remote call is about to be made.
- [func remoteCall<Act, Err, Res>(on: Act, target: RemoteCallTarget, invocation: inout LocalTestingDistributedActorSystem.InvocationEncoder, throwing: Err.Type, returning: Res.Type) async throws -> Res](localtestingdistributedactorsystem/remotecall(on:target:invocation:throwing:returning:).md)
  Invoked by the Swift runtime when making a remote call.
- [func remoteCallVoid<Act, Err>(on: Act, target: RemoteCallTarget, invocation: inout LocalTestingDistributedActorSystem.InvocationEncoder, throwing: Err.Type) async throws](localtestingdistributedactorsystem/remotecallvoid(on:target:invocation:throwing:).md)
  Invoked by the Swift runtime when making a remote call.
- [func resignID(LocalTestingDistributedActorSystem.ActorID)](localtestingdistributedactorsystem/resignid(_:).md)
  Called during when a distributed actor is deinitialized, or fails to initialize completely (e.g. by throwing out of an `init` that did not completely initialize all of the actors stored properties yet).
- [func resolve<Act>(id: LocalTestingDistributedActorSystem.ActorID, as: Act.Type) throws -> Act?](localtestingdistributedactorsystem/resolve(id:as:).md)
  Resolves a local or remote [`LocalTestingDistributedActorSystem.ActorID`](localtestingdistributedactorsystem/actorid.md) to a reference to given actor, or throws if unable to.
### Type Aliases
- [LocalTestingDistributedActorSystem.ActorID](localtestingdistributedactorsystem/actorid.md)
  The type ID that will be assigned to any distributed actor managed by this actor system.
- [LocalTestingDistributedActorSystem.InvocationDecoder](localtestingdistributedactorsystem/invocationdecoder.md)
  Type of [`DistributedTargetInvocationDecoder`](distributedtargetinvocationdecoder.md) that should be used when decoding invocations during [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](localtestingdistributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md) calls.
- [LocalTestingDistributedActorSystem.InvocationEncoder](localtestingdistributedactorsystem/invocationencoder.md)
  Type of [`DistributedTargetInvocationEncoder`](distributedtargetinvocationencoder.md) that should be used when the Swift runtime needs to encode a distributed target call into an encoder, before passing it off to `remoteCall(...)`.
- [LocalTestingDistributedActorSystem.ResultHandler](localtestingdistributedactorsystem/resulthandler.md)
  The type of the result handler which will be offered the results returned by a distributed function invocation called via [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](localtestingdistributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md).
- [LocalTestingDistributedActorSystem.SerializationRequirement](localtestingdistributedactorsystem/serializationrequirement.md)
  The serialization requirement that will be applied to all distributed targets used with this system.
### Default Implementations
- [DistributedActorSystem Implementations](localtestingdistributedactorsystem/distributedactorsystem-implementations.md)

## Relationships

### Conforms To
- [DistributedActorSystem](distributedactorsystem.md)
- [Sendable](../swift/sendable.md)

## See Also

- [struct LocalTestingActorID](localtestingactorid.md)
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [struct LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [class LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [struct LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem)*