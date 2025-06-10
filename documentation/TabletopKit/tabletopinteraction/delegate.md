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

Implement the [`update(interaction:)`](tabletopinteraction/delegate/update(interaction:).md) method to take an appropriate action depending on the equipment and the phase of the interaction. For example, turn a card face up if a player flips it over or toss a die when a gesture ends.

## Topics

### Taking actions
- [func update(interaction: TabletopInteraction)](tabletopinteraction/delegate/update(interaction:).md)
### Instance Methods
- [func onTossStart(interaction: TabletopInteraction, outcomes: [TabletopInteraction.TossOutcome])](tabletopinteraction/delegate/ontossstart(interaction:outcomes:).md)
  Implement `onTossStart(interaction:outcomes)` to be notified that the toss has just started simulating and to receive the outcome of the simulation. If the provided outcome is set to the equipment via actions, the equipment will retain the final state of the simulation even after the simulation ended.
- [func shouldAcceptDirectInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewDirectInteractionIntent](tabletopinteraction/delegate/shouldacceptdirectinteraction(initialvalue:handoffvalue:).md)
  Implement `shouldAcceptDirectInteraction(initialValue:handoffValue)` to provide the constants and initial configuration for the new direct interaction, and to decide if the new interaction should be accepted or rejected. If the function is not implemented, the default implementation will be used, which will call into the more generic `shouldAcceptInteraction(initialValue:handoffValue)`.
- [func shouldAcceptIndirectInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewIndirectInteractionIntent](tabletopinteraction/delegate/shouldacceptindirectinteraction(initialvalue:handoffvalue:).md)
  Implement `shouldAcceptIndirectInteraction(initialValue:handoffValue)` to provide the constants and initial configuration for the new indirect interaction, and to decide if the new interaction should be accepted or rejected. If the function is not implemented, the default implementation will be used, which will call into the more generic `shouldAcceptInteraction(initialValue:handoffValue)`.
- [func shouldAcceptInteraction(initialValue: TabletopInteraction.Value, handoffValue: TabletopInteraction.Value?) -> TabletopInteraction.NewInteractionIntent](tabletopinteraction/delegate/shouldacceptinteraction(initialvalue:handoffvalue:).md)
  Implement `shouldAcceptInteraction(initialValue:handoffValue)` to provide the initial configuration for new interactions, and to decide if a new interaction should be accepted or rejected. If this function is not implemented, the default implementation will be used which will reject all handoff interactions and will accept all other interactions providing the default configuration.

## See Also

- [func addActions(some Sequence<any TabletopAction>)](tabletopinteraction/addactions(_:).md)
  Submit a collection of actions tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func toss(equipmentID: EquipmentIdentifier, as: TossableRepresentation, linearVelocity: Vector3D?, angularVelocity: Vector3D?)](tabletopinteraction/toss(equipmentid:as:linearvelocity:angularvelocity:).md)
  Begins a simulation of a toss of the equipment with the specificied parameters. Equipment that begins a toss in the same TabletopInteraction may interact with each other as well as the game’s boundary.
- [func end()](tabletopinteraction/end.md)
  Ends the current interaction.
- [func cancel()](tabletopinteraction/cancel.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/delegate)*