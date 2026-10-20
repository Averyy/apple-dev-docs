# TabletopInteraction.Value

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

A structure that provides the details about an interaction, such as the phase of the gesture and position of the equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Value
```

## Topics

### Getting information about the equipment and game
- [var startingEquipmentID: EquipmentIdentifier](./value-swift.struct/startingequipmentid.md)
  The equipment the interaction was started with
- [var controlledEquipmentID: EquipmentIdentifier](./value-swift.struct/controlledequipmentid.md)
  The equipment the interaction is currently controlling
- [var allowedDestinations: TabletopInteraction.AllowedDestinations](./value-swift.struct/alloweddestinations.md)
  The allowed destinations that this interaction can target
### Getting the phases
- [var gesturePhase: TabletopInteraction.Value.Phase?](./value-swift.struct/gesturephase.md)
  the current phase of the gesture
- [var phase: TabletopInteraction.Value.Phase](./value-swift.struct/phase-swift.property.md)
  the current phase of the overall interaction
- [TabletopInteraction.Value.Phase](./value-swift.struct/phase-swift.enum.md)
  The stages of players interacting with equipment on the table.
### Getting the gestures
- [var gesture: TabletopInteraction.Value.Gesture?](./value-swift.struct/gesture-swift.property.md)
  If this is interaction is currently gesture driven, contains gesture specific additional information
- [TabletopInteraction.Value.Gesture](./value-swift.struct/gesture-swift.struct.md)
  A structure that provides details specific to a gesture driven interaction.
### Getting the proposed locations
- [var proposedDestination: TabletopInteraction.Destination?](./value-swift.struct/proposeddestination.md)
  The proposed destination of the main interaction object, computed from the current pose of the object. During a toss simulation, the proposed destination is only updated if there is only one tossed equipment and it is the currently controlled equipment.
- [var proposedFlip: Bool](./value-swift.struct/proposedflip.md)
  Was the object flipped from the start of this interaction
### Getting the position and location
- [var pose: Pose3D](./value-swift.struct/pose.md)
  The current pose of the main interaction object
- [var locationOnTable: TableVisualState.Point2D?](./value-swift.struct/locationontable.md)
  The 2D location of the main interaction object
- [var endLocation: Point3D?](./value-swift.struct/endlocation.md)
  The expected end location
- [var endLocationOnTable: TableVisualState.Point2D?](./value-swift.struct/endlocationontable.md)
  The expected end 2D location of the main interaction object
### Getting identifiers
- [var id: TabletopInteraction.Value.ID](./value-swift.struct/id.md)
  Identifier to recognize different interactions from one another
- [var playerID: PlayerIdentifier](./value-swift.struct/playerid.md)
  The player who is performing the interaction
### Getting the interaction properties
- [var configuration: TabletopInteraction.Configuration](./value-swift.struct/configuration.md)
  The current configuration of this interaction
- [var constants: TabletopInteraction.Constants](./value-swift.struct/constants.md)
  The constants of this interaction
- [var initialPose: Pose3D](./value-swift.struct/initialpose.md)
  The pose of the equipment that the interaction was started with

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the value of the interaction
- [var value: TabletopInteraction.Value](./value-swift.property.md)
  The current value belonging to this interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct)*