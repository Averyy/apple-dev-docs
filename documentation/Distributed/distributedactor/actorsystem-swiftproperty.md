# actorSystem

**Framework**: Distributed  
**Kind**: property  
**Required**: Yes

The [`DistributedActorSystem`](distributedactorsystem.md) that is managing this distributed actor.

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
nonisolated
var actorSystem: Self.ActorSystem { get }
```

#### Discussion

It is immutable and equal to the system assigned during the distributed actor’s local initializer (or to the system passed to the [`resolve(id:using:)`](distributedactor/resolve(id:using:).md) static function).

#### Synthesized Property

In concrete distributed actor declarations, a witness for this protocol requirement is synthesized by the compiler.

It is required to assign an initial value to the `actorSystem` property inside a distributed actor’s designated initializer. Semantically, it can be treated as a `let` declaration, that must be assigned in order to fully-initialize the instance.

If a distributed actor declares no initializer, its default initializer will take the shape of `init(actorSystem:)`, and initialize this property using the passed [`DistributedActorSystem`](distributedactorsystem.md). If any user-defined initializer exists, the default initializer is not synthesized, and all the user-defined initializers must take care to initialize this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactor/actorsystem-swift.property)*