# volumetric(layout:animationDuration:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

Use the volumetric layout to provide 3d poses for the immediate children directly.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func volumetric(layout: [EquipmentPose3D], animationDuration: Double? = nil) -> Self
```

Available when `Self` is `DefaultEquipmentLayout`.

## Parameters

- `layout`: An array of id and 3d pose for each child.
- `animationDuration`: The duration of the transition between the current pose and the new pose. If zero or less than zero the new pose will be applied instantly. If not specified a default duration will be used. If the layout contains poses for equipment that are not immediate children, those poses will be ignored. If the pose of some immediate children is not provided, the previous pose and duration will be used if available.

## See Also

### Laying out equipment
- [static func planarOverlapping(layout: [EquipmentPose2D], animationDuration: Double?) -> Self](./planaroverlapping%28layout,animationduration%29.md)
  Use the overlapping layout to provide 2d poses for the immediate children and let TabletopKit determine their height and pitch/roll.
- [static func planarStacked(layout: [EquipmentPose2D], animationDuration: Double?) -> Self](./planarstacked%28layout,animationduration%29.md)
  Use the stacked layout to provide 2d poses for the immediate children and let TabletopKit determine their height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentlayout/volumetric(layout:animationduration:))*