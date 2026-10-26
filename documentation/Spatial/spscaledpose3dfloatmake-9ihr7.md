# SPScaledPose3DFloatMake

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPScaledPose3DFloat SPScaledPose3DFloatMake(SPPoint3DFloat position, SPRotation3DFloat rotation, float scale);
```

#### Return Value

A new scaled pose structure.

#### Discussion

Returns a scaled pose with the specified position, rotation, and scale.

## Parameters

- `position`: A point structure that specifies the position of the scaled pose.
- `rotation`: A rotation structure that specifies the rotation of the scaled pose.
- `scale`: The uniform scale of the pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatmake-9ihr7)*