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
static SPRotation3DFloat SPRotation3DFloatMakeLookAt(SPVector3DFloat forward, SPVector3DFloat up);
```

#### Return Value

A new rotation stucture.

#### Discussion

Returns a rotation with the specified forward and up vectors.

> **Note**: This function creates a rotation where @p +z is forward.

## Parameters

- `forward`: The forward direction.
- `up`: The up direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dfloatmakelookat-3zivr)*