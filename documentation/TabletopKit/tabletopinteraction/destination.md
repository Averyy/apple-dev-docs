# TabletopInteraction.Destination

**Framework**: TabletopKit  
**Kind**: struct

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
- [let equipmentID: EquipmentIdentifier](tabletopinteraction/destination/equipmentid.md)
  The interaction’s destination equipment.
### Getting the interaction pose
- [let pose: TableVisualState.Pose2D](tabletopinteraction/destination/pose.md)
  The 2D position and orientation of the interaction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setAllowedDestinations(TabletopInteraction.AllowedDestinations)](tabletopinteraction/setalloweddestinations(_:).md)
  Sets which equipment the interaction can target.
- [TabletopInteraction.AllowedDestinations](tabletopinteraction/alloweddestinations.md)
  The possible destinations of equipment in an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/destination)*