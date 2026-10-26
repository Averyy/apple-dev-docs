# SPRotation3DFloatAlmostEqualToRotation

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
static bool SPRotation3DFloatAlmostEqualToRotation(SPRotation3DFloat r1, SPRotation3DFloat r2, float tolerance);
```

#### Return Value

A Boolean value that indicates whether the two rotations are equal within the specified absolute tolerance.

#### Discussion

Returns a Boolean value that indicates whether the two rotations are equal within the specified absolute tolerance.

> **Note**: The Spatial default tolerance is @p sqrt(**DBL_EPSILON**) .

## Parameters

- `r1`: The first rotation.
- `r2`: The first rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dfloatalmostequaltorotation-2krut)*