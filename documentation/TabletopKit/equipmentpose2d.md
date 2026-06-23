# EquipmentPose2D

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the position and rotation of equipment on the XZ plane.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct EquipmentPose2D
```

## Topics

### Creating an equipment pose object
- [init(id: EquipmentIdentifier, pose: TableVisualState.Pose2D)](equipmentpose2d/init(id:pose:).md)
  Creates a position and rotation on the table for a specific piece of equipment.
### Getting equipment pose properties
- [var id: EquipmentIdentifier](equipmentpose2d/id.md)
  The unique identifier for the equipment.
- [var pose: TableVisualState.Pose2D](equipmentpose2d/pose.md)
  The 2D position and rotation of equipment on the table.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol EquipmentLayout](equipmentlayout.md)
  A protocol for objects that describe the layout of equipment.
- [struct DefaultEquipmentLayout](defaultequipmentlayout.md)
  An object that provides a standard configuration for equipment layout.
- [struct EquipmentPose3D](equipmentpose3d.md)
  An object that represents the 3D position and orientation of equipment on the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentpose2d)*