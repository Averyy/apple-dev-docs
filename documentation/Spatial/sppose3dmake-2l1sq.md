# SPPose3DMake

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPPose3D SPPose3DMake(SPPoint3D position, SPRotation3D rotation);
```

#### Return Value

A new pose structure.

#### Discussion

Returns a pose with the specified position and rotation.

## Parameters

- `position`: A point structure that specifies the position of the pose.
- `rotation`: A rotation structure that specifies the rotation of the pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppose3dmake-2l1sq)*