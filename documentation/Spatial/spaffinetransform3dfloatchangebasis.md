# SPAffineTransform3DFloatChangeBasis

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
static SPAffineTransform3DFloat SPAffineTransform3DFloatChangeBasis(SPAffineTransform3DFloat transform, SPAffineTransform3DFloat from, SPAffineTransform3DFloat to);
```

#### Return Value

A new affine transform structure or `SPAffineTransform3DInvalid`.

#### Discussion

Returns a new affine transform structure by applying a change-of-basis.

## Parameters

- `transform`: The source transform.
- `from`: The old basis.
- `to`: The new basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3dfloatchangebasis)*