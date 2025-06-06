# toss(equipmentID:as:linearVelocity:angularVelocity:)

**Framework**: TabletopKit  
**Kind**: method

Begins a simulation of a toss of the equipment with the specificied parameters. Equipment that begins a toss in the same TabletopInteraction may interact with each other as well as the game’s boundary.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func toss(equipmentID: EquipmentIdentifier, as representation: TossableRepresentation, linearVelocity: Vector3D? = nil, angularVelocity: Vector3D? = nil)
```

## Parameters

- `equipmentID`: The equipment ID to use in the toss simulation.
- `representation`: The representation that the toss simulation will treat the equipment as.
- `linearVelocity`: The linear velocity the toss begins with. If nil, the simulation will use the interaction’s current linear velocity.
- `angularVelocity`: The angular velocity the toss begins with. If nil, the simulation will use the interaction’s current angular velocity.

## See Also

- [TabletopInteraction.Delegate](tabletopinteraction/delegate.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [func addAction(some TabletopAction)](tabletopinteraction/addaction(_:).md)
- [func addActions(some Sequence<any TabletopAction>)](tabletopinteraction/addactions(_:).md)
- [func end()](tabletopinteraction/end.md)
  Ends the current interaction.
- [func cancel()](tabletopinteraction/cancel.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/toss(equipmentid:as:linearvelocity:angularvelocity:))*