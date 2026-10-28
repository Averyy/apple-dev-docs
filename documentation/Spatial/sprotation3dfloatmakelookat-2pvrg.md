# SPRotation3DFloatMakeLookAt

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
static SPRotation3DFloat SPRotation3DFloatMakeLookAt(SPPoint3DFloat position, SPPoint3DFloat target, SPVector3DFloat up);
```

## Return Value

A new rotation stucture.

## Discussion

Returns a rotation that’s the look at direction from the position position to the target.

> **Note**: This function creates a rotation where @p +z is forward.

## Parameters

- `position`: The eye position.
- `target`: The point that the rotation looks at.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dfloatmakelookat-2pvrg)*