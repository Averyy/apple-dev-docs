# SPVector3DSmoothstep

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
static SPVector3D SPVector3DSmoothstep(SPVector3D edge0, SPVector3D edge1, SPVector3D x);
```

#### Return Value

A new vector with each element set to `0` if `x <= edge0`, `1` if `x >= edge1`, and a Hermite interpolation between `0` and `1` if `edge0 < x < edge1`.

#### Discussion

Returns a Spatial vector that represents the smooth interpolation at @p x between two vectors.

## Parameters

- `edge0`: The lower edge of the interpolation function.
- `edge1`: The upper edge of the interpolation function.
- `x`: The value that the function interpolates at.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spvector3dsmoothstep)*