# resolve(id:as:)

**Framework**: Distributed  
**Kind**: method

Resolves a local or remote [`LocalTestingDistributedActorSystem.ActorID`](localtestingdistributedactorsystem/actorid.md) to a reference to given actor, or throws if unable to.

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
final func resolve<Act>(id: LocalTestingDistributedActorSystem.ActorID, as actorType: Act.Type) throws -> Act? where Act : DistributedActor
```

#### Discussion

The returned value is either a local actor or proxy to a remote actor.

This function is not intended to be used directly, but instead is called by the Swift runtime whenever ``DistributedActor/resolve(id:using:)`or  a concrete distributed actor's`init(from:)` is invoked.

This function should either return an existing actor reference, or `nil` to signal that a remote distributed actor “proxy” should be created for this [`LocalTestingDistributedActorSystem.ActorID`](localtestingdistributedactorsystem/actorid.md). If the resolve fails, meaning that it can neither locate a local actor managed by this actor system, nor identify that the identity is located on some remote actor system, then this function should throw.

```swift
distributed actor Worker { /* ... */ }

// the following internally calls actorSystem.resolve(id: id, as: Worker.self)
let worker: Worker = try  Worker.resolve(id: id, using: actorSystem)
```

If this function returns correctly, the returned actor reference is immediately usable. It may not necessarily imply the strict  of a remote actor the identity was pointing towards, e.g. when a remote system allocates actors lazily as they are first time messaged to, however this should not be a concern of the sending side.

Detecting liveness of such remote actors shall be offered / by transport libraries by other means, such as “watching an actor for termination” or similar.

> **Note**: When unable to confirm if the `id` is correct, the resolved actor does not match the expected `actorType`, or any other internal validation error within the actor system’s resolve process occurs.

When unable to confirm if the `id` is correct, the resolved actor does not match the expected `actorType`, or any other internal validation error within the actor system’s resolve process occurs.

## Parameters

- `id`: The   to resolve an actor reference for
- `actorType`: The type of distributed actor the ID is expected to point at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestingdistributedactorsystem/resolve(id:as:))*