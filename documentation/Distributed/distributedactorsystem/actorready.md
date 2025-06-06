# actorReady(_:)

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

Invoked during a distributed actor’s initialization, as soon as it becomes fully initialized.

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
func actorReady<Act>(_ actor: Act) where Act : DistributedActor, Self.ActorID == Act.ID
```

#### Discussion

The system is expected to store the reference to this actor, and maintain an `ActorID: DistributedActor` mapping for the purpose of implementing the `resolve(id:as:)` method.

The system usually should NOT retain the passed reference, and it will be informed via [`resignID(_:)`](distributedactorsystem/resignid(_:).md) when the actor has been deallocated so it can remove the stale reference from its internal `ActorID: DistributedActor` mapping.

The [`id`](distributedactor/id.md) of the passed actor must be an [`ActorID`](distributedactorsystem/actorid.md) that this system previously has assigned.

If `actorReady` gets called with some unknown ID, it should crash immediately as it signifies some very unexpected use of the system.

## Parameters

- `actor`: Reference to the (local) actor that was just fully initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedactorsystem/actorready(_:))*