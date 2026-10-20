# toss(equipmentID:as:linearVelocity:angularVelocity:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

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

### Performing actions
- [TabletopInteraction.Delegate](./delegate.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [TabletopInteraction.TossOutcome](./tossoutcome.md)
  An object representing the final outcome of tossing one equipment, as it appears at the end of its simulation.
- [func addAction(some TabletopAction)](./addaction%28_%29-1cety.md)
  Submit an action tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func addAction(some CustomAction)](./addaction%28_%29-4rx16.md)
  Submit a custom action tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func addActions(some Sequence<any TabletopAction>)](./addactions%28_%29.md)
  Submit a collection of actions tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func end()](./end%28%29.md)
  Ends the current interaction.
- [func cancel()](./cancel%28%29.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/toss(equipmentid:as:linearvelocity:angularvelocity:))*