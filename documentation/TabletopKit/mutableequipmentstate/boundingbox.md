# boundingBox

**Framework**: TabletopKit  
**Kind**: property  
**Required**: Yes

A 3D bounding box that encloses the equipment.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
override var boundingBox: Rect3D { get set }
```

#### Discussion

This bounding box is object oriented, so remains the same regardless of the equipment orientation.

## See Also

- [var pose: TableVisualState.Pose2D](mutableequipmentstate/pose.md)
  The 2D position and rotation of the equipment relative to the parent equipment, or table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/mutableequipmentstate/boundingbox)*