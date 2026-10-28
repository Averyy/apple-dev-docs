# SPSize3DFloatUnapplyAffineTransform

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
static SPSize3DFloat SPSize3DFloatUnapplyAffineTransform(SPSize3DFloat size, SPAffineTransform3DFloat transform);
```

## Return Value

The transformed size.

## Discussion

Returns a size that’s transformed by the inverse of the specified affine transform.

## Parameters

- `size`: The source size.
- `transform`: The affine transform that the function unapplies to the size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spsize3dfloatunapplyaffinetransform)*