# TabletopInteraction

**Framework**: TabletopKit  
**Kind**: class

A protocol for objects that manage the entire flow of players interacting with equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
class TabletopInteraction
```

#### Overview

Conform to the [`TabletopInteraction.Delegate`](tabletopinteraction/delegate.md) protocol to take an appropriate action, depending on the equipment and the phase of the interaction. For example, move equipment or toss a die when a gesture ends.

```swift
struct MoveInteraction: TabletopInteraction.Delegate {
    func update(interaction: TabletopKit.TabletopInteraction) {
        let equipment = interaction.value.controlledEquipmentID
        guard let destination = interaction.value.proposedDestination else {
            return
        }
        
        if interaction.value.phase == .ended {
            interaction.addAction(.moveEquipment(matching: equipment, childOf: destination.equipmentID, pose: destination.pose))
        }
    }
}
```

To get information about the equipment that the interaction applies to, use the [`value`](tabletopinteraction/value-swift.property.md) property. To get the phase of the interaction or gesture, use the `Value` [`gesturePhase`](tabletopinteraction/value-swift.struct/gesturephase.md) or [`phase`](tabletopinteraction/value-swift.struct/phase-swift.property.md) properties.

Then execute actions — for example, move equipment when the phase ends — using the [`addAction(_:)`](tabletopinteraction/addaction(_:).md) or [`addActions(_:)`](tabletopinteraction/addactions(_:).md) method.

To start an interaction programmatically, use the `TabletopGame` [`startInteraction(onEquipmentID:)`](tabletopgame/startinteraction(onequipmentid:).md) method.

## Topics

### Performing actions
- [TabletopInteraction.Delegate](tabletopinteraction/delegate.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [func addAction(some TabletopAction)](tabletopinteraction/addaction(_:).md)
- [func addActions(some Sequence<any TabletopAction>)](tabletopinteraction/addactions(_:).md)
- [func toss(equipmentID: EquipmentIdentifier, as: TossableRepresentation, linearVelocity: Vector3D?, angularVelocity: Vector3D?)](tabletopinteraction/toss(equipmentid:as:linearvelocity:angularvelocity:).md)
  Begins a simulation of a toss of the equipment with the specificied parameters. Equipment that begins a toss in the same TabletopInteraction may interact with each other as well as the game’s boundary.
- [func end()](tabletopinteraction/end.md)
  Ends the current interaction.
- [func cancel()](tabletopinteraction/cancel.md)
  Cancels the current interaction. All actions added to the interaction will also be cancelled.
### Getting the value of the interaction
- [var value: TabletopInteraction.Value](tabletopinteraction/value-swift.property.md)
  The current value belonging to this interaction.
- [TabletopInteraction.Value](tabletopinteraction/value-swift.struct.md)
  A structure that provides the details about an interaction, such as the phase of the gesture and position of the equipment.
### Setting information about the equipment and pose
- [func setControlledEquipment(matching: EquipmentIdentifier)](tabletopinteraction/setcontrolledequipment(matching:).md)
  Replace the current controlled equipment with a different one
- [func setPose(Pose3D)](tabletopinteraction/setpose(_:).md)
  Sets the pose of the controlled `Equipment`.
### Managing the interaction destination
- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](tabletopinteraction/setalloweddestinations(_:).md)
  Sets which equipment the interaction can target.
- [TabletopInteraction.AllowedDestinations](tabletopinteraction/alloweddestinations.md)
  The possible destinations of equipment in an interaction.
- [TabletopInteraction.Destination](tabletopinteraction/destination.md)
  An object that represents the destination position and orientation of equipment in an interaction.
### Getting the interaction identifier
- [TabletopInteraction.Identifier](tabletopinteraction/identifier.md)
  A unique identifier for interactions.
### Structures
- [TabletopInteraction.Configuration](tabletopinteraction/configuration.md)
  A struct containing the parameters that affect the behavior of the interaction.
### Instance Methods
- [func setConfiguration(TabletopInteraction.Configuration)](tabletopinteraction/setconfiguration(_:).md)
  Sets the configuration of this interaction.
### Enumerations
- [TabletopInteraction.NewInteractionIntent](tabletopinteraction/newinteractionintent.md)
  The possible outcomes when a new interaction is about to be started.

## See Also

- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](tablecursor.md)
  A visual indicator that represents the destination of player interactions with equipment.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction)*