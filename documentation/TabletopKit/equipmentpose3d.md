# EquipmentPose3D

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the 3D position and orientation of equipment on the table.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct EquipmentPose3D
```

## Topics

### Creating an equipment pose object
- [init(id: EquipmentIdentifier, pose: Pose3D)](equipmentpose3d/init(id:pose:).md)
  Creates a position and orientation on the table for a specific piece of equipment.
### Getting equipment pose properties
- [var id: EquipmentIdentifier](equipmentpose3d/id.md)
- [var pose: Pose3D](equipmentpose3d/pose.md)
  The 3D position and orientation of equipment on the table.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol EquipmentLayout](equipmentlayout.md)
  A protocol for objects that describe the layout of equipment.
- [struct DefaultEquipmentLayout](defaultequipmentlayout.md)
  An object that provides a standard configuration for equipment layout.
- [struct EquipmentPose2D](equipmentpose2d.md)
  An object that represents the position and rotation of equipment on the XZ plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentpose3d)*