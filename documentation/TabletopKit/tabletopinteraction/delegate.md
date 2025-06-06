# TabletopInteraction.Delegate

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for objects that manage the entire flow of players interacting with equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol Delegate
```

#### Overview

Implement the [`update(interaction:)`](tabletopinteraction/delegate/update(interaction:).md) method to take an appropriate action depending on the equipment and the phase of the interaction. For example, turn a card face up if a player flips it over or toss a die when a gesture ends. Implement the `shouldAcceptInteraction(initialValue:handoffValue)` method to allow handoff interactions, to provide the initial configuration for new interactions, and to decide if a new interaction should be rejected. If `shouldAcceptInteraction(initialValue:handoffValue)` is not implemented, all handoff interactions will be rejected.

## Topics

### Taking actions
- [func update(interaction: TabletopInteraction)](tabletopinteraction/delegate/update(interaction:).md)
### Instance Methods
- [func shouldAcceptInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewInteractionIntent](tabletopinteraction/delegate/shouldacceptinteraction(initialvalue:handoffvalue:).md)

## See Also

- [func addAction(some TabletopAction)](tabletopinteraction/addaction(_:).md)
- [func addActions(some Sequence<any TabletopAction>)](tabletopinteraction/addactions(_:).md)
- [func toss(equipmentID: EquipmentIdentifier, as: TossableRepresentation, linearVelocity: Vector3D?, angularVelocity: Vector3D?)](tabletopinteraction/toss(equipmentid:as:linearvelocity:angularvelocity:).md)
  Begins a simulation of a toss of the equipment with the specificied parameters. Equipment that begins a toss in the same TabletopInteraction may interact with each other as well as the game’s boundary.
- [func end()](tabletopinteraction/end.md)
  Ends the current interaction.
- [func cancel()](tabletopinteraction/cancel.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate)*