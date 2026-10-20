# TabletopInteraction.Destination

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents the destination position and orientation of equipment in an interaction.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Destination
```

#### Overview

The position and orientation can be relative to either a piece of equipment or the table.

## Topics

### Getting the destination equipment
- [let equipmentID: EquipmentIdentifier](./destination/equipmentid.md)
  The interaction’s destination equipment.
### Getting the interaction pose
- [let pose: TableVisualState.Pose2D](./destination/pose.md)
  The 2D position and orientation of the interaction.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the interaction destination
- [func setConfiguration(TabletopInteraction.Configuration)](./setconfiguration%28_%29.md)
  Sets the configuration of this interaction.
- [TabletopInteraction.Configuration](./configuration.md)
- [TabletopInteraction.AllowedDestinations](./alloweddestinations.md)
  The possible destinations of equipment in an interaction.
- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](./setalloweddestinations%28_%29.md)
  Sets which equipment the interaction can target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/destination)*