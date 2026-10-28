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
static SPScaledPose3DFloat SPScaledPose3DFloatMakeLookAt(SPVector3DFloat forward, float scale, SPVector3DFloat up);
```

## Return Value

A new scaled pose stucture.

## Discussion

Returns a scaled pose with the specified forward and up vectors.

> **Note**: This function creates a scaled pose where @p +z is forward.

## Parameters

- `forward`: The forward direction.
- `scale`: The uniform scale of the pose.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spscaledpose3dfloatmakelookat-4kx9a)*