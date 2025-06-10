# boundingBox

**Framework**: TabletopKit  
**Kind**: property  
**Required**: Yes

A 3D bounding box that encloses the equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var boundingBox: Rect3D { get }
```

#### Discussion

This bounding box is object oriented, so remains the same regardless of the equipment orientation.

## See Also

- [var pose: TableVisualState.Pose2D](equipmentstate/pose.md)
  The 2D position and rotation of the equipment relative to the parent equipment, or table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/equipmentstate/boundingbox)*