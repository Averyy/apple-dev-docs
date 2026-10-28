# SPScaledPose3DFloatMakeLookAt

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
static SPScaledPose3DFloat SPScaledPose3DFloatMakeLookAt(SPPoint3DFloat position, SPPoint3DFloat target, float scale, SPVector3DFloat up);
```

## Return Value

A new scaled pose structure.

## Discussion

Returns a scaled pose at the specified position with the rotation towards the target.

## Parameters

- `position`: A point structure that specifies the position of the scaled pose.
- `target`: The point that the scaled pose orients towards.
- `scale`: The uniform scale of the pose.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatmakelookat-61u16)*