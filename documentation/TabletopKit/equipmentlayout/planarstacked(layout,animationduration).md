# planarStacked(layout:animationDuration:)

**Framework**: TabletopKit  
**Kind**: method

Use the stacked layout to provide 2d poses for the immediate children and let TabletopKit determine their height.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func planarStacked(layout: [EquipmentPose2D], animationDuration: Double? = nil) -> Self
```

#### Discussion

The height of the children is calculated by going over each equipment in the layout in the provided order and moving it to the lowest possible position so that it touches either the table or any of the siblings already placed.

If the layout contains poses for equipment that are not immediate children, those poses will be ignored. If the pose of some immediate children is not provided, the pose in their EquipmentState is used instead.

## Parameters

- `layout`: An array of id and 2d pose for each child.
- `animationDuration`: The duration of the transition between the current pose and the new pose. If zero or less than zero the new pose will be applied instantly. If not specified a default duration will be used.

## See Also

- [static func planarOverlapping(layout: [EquipmentPose2D], animationDuration: Double?) -> Self](equipmentlayout/planaroverlapping(layout:animationduration:).md)
  Use the overlapping layout to provide 2d poses for the immediate children and let TabletopKit determine their height and pitch/roll.
- [static func volumetric(layout: [EquipmentPose3D], animationDuration: Double?) -> Self](equipmentlayout/volumetric(layout:animationduration:).md)
  Use the volumetric layout to provide 3d poses for the immediate children directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentlayout/planarstacked(layout:animationduration:))*