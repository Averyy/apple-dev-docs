# TabletopInteraction.Value

**Framework**: TabletopKit  
**Kind**: struct

A structure that provides the details about an interaction, such as the phase of the gesture and position of the equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Value
```

## Topics

### Getting information about the equipment and game
- [var startingEquipmentID: EquipmentIdentifier](tabletopinteraction/value-swift.struct/startingequipmentid.md)
  The equipment the interaction was started with
- [var controlledEquipmentID: EquipmentIdentifier](tabletopinteraction/value-swift.struct/controlledequipmentid.md)
  The equipment the interaction is currently controlling
- [var allowedDestinations: TabletopInteraction.AllowedDestinations](tabletopinteraction/value-swift.struct/alloweddestinations.md)
  The allowed destinations that this interaction can target
### Getting the phases
- [var gesturePhase: TabletopInteraction.Value.Phase?](tabletopinteraction/value-swift.struct/gesturephase.md)
  the current phase of the gesture
- [var phase: TabletopInteraction.Value.Phase](tabletopinteraction/value-swift.struct/phase-swift.property.md)
  the current phase of the overall interaction
- [TabletopInteraction.Value.Phase](tabletopinteraction/value-swift.struct/phase-swift.enum.md)
  The stages of players interacting with equipment on the table.
### Getting the proposed locations
- [var proposedDestination: TabletopInteraction.Destination?](tabletopinteraction/value-swift.struct/proposeddestination.md)
  The proposed destination of the main interaction object, computed from the current pose of the object. During a toss simulation, the proposed destination is only updated if there is only one tossed equipment and it is the currently controlled equipment.
- [var proposedFlip: Bool](tabletopinteraction/value-swift.struct/proposedflip.md)
  Was the object flipped from the start of this interaction
### Getting the position and location
- [var pose: Pose3D](tabletopinteraction/value-swift.struct/pose.md)
  The current pose of the main interaction object
- [var locationOnTable: TableVisualState.Point2D?](tabletopinteraction/value-swift.struct/locationontable.md)
  The 2D location of the main interaction object
- [var endLocation: Point3D?](tabletopinteraction/value-swift.struct/endlocation.md)
  The expected end location
- [var endLocationOnTable: TableVisualState.Point2D?](tabletopinteraction/value-swift.struct/endlocationontable.md)
  The expected end 2D location of the main interaction object
### Getting identifiers
- [var id: TabletopInteraction.Value.ID](tabletopinteraction/value-swift.struct/id.md)
  Identifier to recognize different interactions from one another
- [var playerID: PlayerIdentifier](tabletopinteraction/value-swift.struct/playerid.md)
  The player who is performing the interaction
### Structures
- [TabletopInteraction.Value.Gesture](tabletopinteraction/value-swift.struct/gesture-swift.struct.md)
  A structure that provides details specific to a gesture driven interaction.
### Instance Properties
- [var configuration: TabletopInteraction.Configuration](tabletopinteraction/value-swift.struct/configuration.md)
  The configuration of this interaction
- [var gesture: TabletopInteraction.Value.Gesture?](tabletopinteraction/value-swift.struct/gesture-swift.property.md)
  If this is interaction is currently gesture driven, contains gesture specific additional information

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var value: TabletopInteraction.Value](tabletopinteraction/value-swift.property.md)
  The current value belonging to this interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct)*