# SPProjectiveTransform3DFloatGetScale

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
static SPSize3DFloat SPProjectiveTransform3DFloatGetScale(SPProjectiveTransform3DFloat transform);
```

#### Return Value

A size structure that represents the transform’s scale.

#### Discussion

Returns a projective transform’s scale.

> **Note**: This function computes the scale from the first three rows of the transform matrix and ignores the fourth row.

## Parameters

- `transform`: The source transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3dfloatgetscale)*