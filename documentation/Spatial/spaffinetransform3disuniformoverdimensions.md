# SPAffineTransform3DIsUniformOverDimensions

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static bool SPAffineTransform3DIsUniformOverDimensions(SPAffineTransform3D transform, SPAxis dimensionFlags);
```

## See Also

### Checking characteristics
- [var isInvertible: Bool](./affinetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [var matrix: simd_double4x3](./affinetransform3d/matrix.md)
  The affine transform’s underlying matrix.
- [var matrix3x3: simd_double3x3](./affinetransform3d/matrix3x3.md)
  The first three columns of an affine transform’s underlying matrix.
- [var matrix4x4: simd_double4x4](./affinetransform3d/matrix4x4.md)
  A 4 x 4 matrix that results from constructing the affine transform’s underlying matrix.
- [SPAffineTransform3DIsValid](./spaffinetransform3disvalid.md)
  A Boolean value that indicates whether the transform is a valid transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3disuniformoverdimensions)*