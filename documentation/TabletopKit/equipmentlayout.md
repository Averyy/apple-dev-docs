# EquipmentLayout

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for objects that describe the layout of equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol EquipmentLayout
```

## Topics

### Laying out equipment
- [static func planarOverlapping(layout: [EquipmentPose2D], animationDuration: Double?) -> Self](equipmentlayout/planaroverlapping(layout:animationduration:).md)
  Use the overlapping layout to provide 2d poses for the immediate children and let TabletopKit determine their height and pitch/roll.
- [static func planarStacked(layout: [EquipmentPose2D], animationDuration: Double?) -> Self](equipmentlayout/planarstacked(layout:animationduration:).md)
  Use the stacked layout to provide 2d poses for the immediate children and let TabletopKit determine their height.
- [static func volumetric(layout: [EquipmentPose3D], animationDuration: Double?) -> Self](equipmentlayout/volumetric(layout:animationduration:).md)
  Use the volumetric layout to provide 3d poses for the immediate children directly.

## Relationships

### Conforming Types
- [DefaultEquipmentLayout](defaultequipmentlayout.md)

## See Also

- [struct DefaultEquipmentLayout](defaultequipmentlayout.md)
  An object that provides a standard configuration for equipment layout.
- [struct EquipmentPose2D](equipmentpose2d.md)
  An object that represents the position and rotation of equipment on the XZ plane.
- [struct EquipmentPose3D](equipmentpose3d.md)
  An object that represents the 3D position and orientation of equipment on the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentlayout)*