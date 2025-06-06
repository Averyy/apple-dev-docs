# Distributed

**Framework**: Distributed  
**Kind**: module

Build systems that run distributed code across multiple processes and devices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

#### Overview

Distributed actors share many characteristics with Swift actors, and include additional isolation checks to ensure location transparency and safety in a distributed environment. Similar to how actors make it easier to write concurrent code that’s safe and correct to run on a single computer, distributed actors make it easier to write code that runs across multiple computers.

![A diagram showing two columns of actors. The left column includes a remote actor reference. The right column includes a local distributed actor. An arrow points from the remote actor reference to the local distributed actor that it refers to.](https://docs-assets.developer.apple.com/published/2bf6622bede5876c3f4d6d1a4e1f1089/distributed-module%402x.png)

You use three main parts when writing code with distributed actors:

- Swift language support for actors and distributed actors. For more information, see [`Concurrency`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in .
- The Distributed module, which includes the types and protocols you need to declare and use distribute actors. For example, it has protocols to which distributed actors and distributed actor systems conform, and structures that encapsulate information about calls to a distributed actor.
- A , also called a cluster runtime, provides an implementation of the [`DistributedActorSystem`](distributedactorsystem.md) protocol and coordinates between the cluster’s nodes. A distributed actor is always part of some distributed actor system; that distributed actor system handles the serialization and networking necessary to perform remote method calls. For local testing, you can use [`LocalTestingDistributedActorSystem`](localtestingdistributedactorsystem.md). For production, you can use the distributed actor system from the [`Swift Distributed Actors`](https://developer.apple.comhttps://github.com/apple/swift-distributed-actors/) library, use another library, or write your own distributed actor system.

## Topics

### Essentials
- [TicTacFish: Implementing a game using distributed actors](../swift/tictacfish_implementing_a_game_using_distributed_actors.md)
  Use distributed actors to take your Swift concurrency and actor-based apps beyond a single process.
### Distributed Actors
- [protocol DistributedActor](distributedactor.md)
  Common protocol to which all distributed actors conform implicitly.
- [protocol DistributedActorSystem](distributedactorsystem.md)
  A distributed actor system underpins and implements all functionality of distributed actors.
- [macro Resolvable()](resolvable().md)
  Enables the attached to protocol to be resolved as remote distributed actor reference.
- [func buildDefaultDistributedRemoteActorExecutor<Act>(Act) -> UnownedSerialExecutor](builddefaultdistributedremoteactorexecutor(_:).md)
  Obtain the unowned `SerialExecutor` that is used by by remote distributed actor references. The executor is shared between all remote default executor remote distributed actors, and it will crash if any job is enqueued on it.
### Remote Calls
- [struct RemoteCallTarget](remotecalltarget.md)
  Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [struct RemoteCallArgument](remotecallargument.md)
  Represents an argument passed to a distributed call target.
- [protocol DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md)
  Used to encode an invocation of a distributed target (method or computed property).
- [protocol DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md)
  Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
- [protocol DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md)
  Protocol a distributed invocation execution’s result handler.
### Local Testing
- [class LocalTestingDistributedActorSystem](localtestingdistributedactorsystem.md)
  A `DistributedActorSystem` designed for local only testing.
- [struct LocalTestingActorID](localtestingactorid.md)
- [typealias LocalTestingActorAddress](localtestingactoraddress.md)
- [struct LocalTestingInvocationEncoder](localtestinginvocationencoder.md)
- [class LocalTestingInvocationDecoder](localtestinginvocationdecoder.md)
- [struct LocalTestingInvocationResultHandler](localtestinginvocationresulthandler.md)
### Errors
- [struct DistributedActorCodingError](distributedactorcodingerror.md)
  Error thrown by distributed actor systems while encountering encoding/decoding issues.
- [protocol DistributedActorSystemError](distributedactorsystemerror.md)
  Error protocol to which errors thrown by any `DistributedActorSystem` should conform.
- [struct ExecuteDistributedTargetError](executedistributedtargeterror.md)
  Error thrown by [`executeDistributedTarget(on:target:invocationDecoder:handler:)`](distributedactorsystem/executedistributedtarget(on:target:invocationdecoder:handler:).md).
- [struct LocalTestingDistributedActorSystemError](localtestingdistributedactorsystemerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Distributed)*