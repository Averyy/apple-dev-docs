# end()

**Framework**: TabletopKit  
**Kind**: method

Ends the current interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func end()
```

## See Also

- [TabletopInteraction.Delegate](tabletopinteraction/delegate.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [func addAction(some TabletopAction)](tabletopinteraction/addaction(_:).md)
- [func addActions(some Sequence<any TabletopAction>)](tabletopinteraction/addactions(_:).md)
- [func toss(equipmentID: EquipmentIdentifier, as: TossableRepresentation, linearVelocity: Vector3D?, angularVelocity: Vector3D?)](tabletopinteraction/toss(equipmentid:as:linearvelocity:angularvelocity:).md)
  Begins a simulation of a toss of the equipment with the specificied parameters. Equipment that begins a toss in the same TabletopInteraction may interact with each other as well as the game’s boundary.
- [func cancel()](tabletopinteraction/cancel.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/end())*