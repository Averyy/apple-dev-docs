# SPAffineTransform3DIsValid

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

A Boolean value that indicates whether the transform is a valid transform.

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
static bool SPAffineTransform3DIsValid(SPAffineTransform3D transform);
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
- [SPAffineTransform3DIsUniformOverDimensions](./spaffinetransform3disuniformoverdimensions.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spaffinetransform3disvalid)*