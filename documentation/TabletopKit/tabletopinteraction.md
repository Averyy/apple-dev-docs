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

Then execute actions — for example, move equipment when the phase ends — using the [`addAction(_:)`](tabletopinteraction/addaction(_:)-1cety.md) or [`addActions(_:)`](tabletopinteraction/addactions(_:).md) method.

To start an interaction programmatically, use the `TabletopGame` [`startInteraction(onEquipmentID:)`](tabletopgame/startinteraction(onequipmentid:).md) method.

## Topics

### Performing actions
- [TabletopInteraction.Delegate](tabletopinteraction/delegate.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [TabletopInteraction.TossOutcome](tabletopinteraction/tossoutcome.md)
  An object representing the final outcome of tossing one equipment, as it appears at the end of its simulation.
- [func addAction(some TabletopAction)](tabletopinteraction/addaction(_:)-1cety.md)
  Submit an action tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func addAction(some CustomAction)](tabletopinteraction/addaction(_:)-4rx16.md)
  Submit a custom action tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
- [func addActions(some Sequence<any TabletopAction>)](tabletopinteraction/addactions(_:).md)
  Submit a collection of actions tied to this interaction. If the interaction gets canceled, all the associated actions will be automatically rolled back.
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
- [func setConfiguration(TabletopInteraction.Configuration)](tabletopinteraction/setconfiguration(_:).md)
  Sets the configuration of this interaction.
- [TabletopInteraction.Configuration](tabletopinteraction/configuration.md)
- [TabletopInteraction.AllowedDestinations](tabletopinteraction/alloweddestinations.md)
  The possible destinations of equipment in an interaction.
- [TabletopInteraction.Destination](tabletopinteraction/destination.md)
  An object that represents the destination position and orientation of equipment in an interaction.
- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](tabletopinteraction/setalloweddestinations(_:).md)
  Sets which equipment the interaction can target.
### Getting the interaction identifier
- [TabletopInteraction.Identifier](tabletopinteraction/identifier.md)
  A unique identifier for interactions.
### Determining the dead zone
- [TabletopInteraction.DeadZone](tabletopinteraction/deadzone.md)
  The dead zone allows to specify how much the input device should move or rotate from its initial pose to start moving the object.
### Handling collision behavior
- [TabletopInteraction.Constants](tabletopinteraction/constants.md)
- [TabletopInteraction.CollisionTargets](tabletopinteraction/collisiontargets.md)
  A set of targets for collision behaviors during an interaction
- [TabletopInteraction.DirectPickupBehavior](tabletopinteraction/directpickupbehavior.md)
  An object that represents the behavior of the pickup phase of the direct interaction. The pickup phase describes how the object moves from its initial pose to the pose it will have when moving rigidly with the input device.
- [TabletopInteraction.DirectInteractionConstants](tabletopinteraction/directinteractionconstants.md)
  An object that represents the parameters of a direct interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.IndirectRotationAlignmentBehavior](tabletopinteraction/indirectrotationalignmentbehavior.md)
  An object that represents how the equipment’s orientation should be automatically aligned during the course of the interaction.
- [TabletopInteraction.IndirectInteractionConstants](tabletopinteraction/indirectinteractionconstants.md)
  An object that represents the parameters of an indirect interaction that cannot be changed while the interaction is active.
- [TabletopInteraction.HoverAlignmentBehavior](tabletopinteraction/hoveralignmentbehavior.md)
  An object that describes how the controlled equipment should behave when approaching a target.
- [TabletopInteraction.HoverAlignmentSource](tabletopinteraction/hoveralignmentsource.md)
  An object representing the types of features that can be auto aligned by the `HoverAlignmentBehavior`
- [TabletopInteraction.ProgrammaticInteractionConstants](tabletopinteraction/programmaticinteractionconstants.md)
  An object that represents the parameters of a programmatic interaction that cannot be changed while the interaction is active.
### Handling interaction intents
- [TabletopInteraction.NewInteractionIntent](tabletopinteraction/newinteractionintent.md)
- [TabletopInteraction.NewDirectInteractionIntent](tabletopinteraction/newdirectinteractionintent.md)
  An object that represent the developer’s intent when a new direct interaction is proposed by the system
- [TabletopInteraction.NewIndirectInteractionIntent](tabletopinteraction/newindirectinteractionintent.md)
  An object that represent the developer’s intent when a new indirect interaction is proposed by the system

## See Also

- [Simulating dice rolls as a component for your game](simulating-dice-rolls-as-a-component-for-your-game.md)
  Create a physically realistic dice game by adding interactive rolling and scoring.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.
- [struct TableCursorIdentifier](tablecursoridentifier.md)
  A unique identifier for cursors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction)*