# TabletopInteraction.TossOutcome

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object representing the final outcome of tossing one equipment, as it appears at the end of its simulation.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct TossOutcome
```

## Topics

### Getting the outcome properties
- [var id: EquipmentIdentifier](./tossoutcome/id.md)
  The identifier of the equipment that was tossed.
- [var pose: TableVisualState.Pose2D](./tossoutcome/pose.md)
  The final pose of the equipment at the end of the toss simulation, in table space.
- [var restingOrientation: Rotation3D](./tossoutcome/restingorientation.md)
  The final resting orientation of the equipment at the end of the toss simulation.
- [var tossableRepresentation: TossableRepresentation](./tossoutcome/tossablerepresentation.md)
  The tossable representation of the equipment that was tossed.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)

## See Also

### Performing actions
- [TabletopInteraction.Delegate](./delegate.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [func addAction(some TabletopAction)](./addaction%28_%29-1cety.md)
  Submit an action tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func addAction(some CustomAction)](./addaction%28_%29-4rx16.md)
  Submit a custom action tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func addActions(some Sequence<any TabletopAction>)](./addactions%28_%29.md)
  Submit a collection of actions tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func toss(equipmentID: EquipmentIdentifier, as: TossableRepresentation, linearVelocity: Vector3D?, angularVelocity: Vector3D?)](./toss%28equipmentid,as,linearvelocity,angularvelocity%29.md)
  Begins a simulation of a toss of the equipment with the specificied parameters. Equipment that begins a toss in the same TabletopInteraction may interact with each other as well as the game’s boundary.
- [func end()](./end%28%29.md)
  Ends the current interaction.
- [func cancel()](./cancel%28%29.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/tossoutcome)*