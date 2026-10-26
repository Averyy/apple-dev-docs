# matrix4x4

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A 4 x 4 matrix that results from constructing the affine transform’s underlying matrix.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var matrix4x4: simd_double4x4 { get }
```

```c
static simd_double4x4 SPAffineTransform3DGet4x4Matrix(SPAffineTransform3D transform);
```

## See Also

### Checking characteristics
- [struct Dimension3DSet](../dimension3dset.md)
  A set of dimensions.
- [var isInvertible: Bool](./isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](./isuniform%28overdimensions%29.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var matrix: simd_double4x3](./matrix.md)
  The affine transform’s underlying matrix.
- [var matrix3x3: simd_double3x3](./matrix3x3.md)
  The first three columns of an affine transform’s underlying matrix.
- [SPAffineTransform3DIsUniformOverDimensions](../spaffinetransform3disuniformoverdimensions.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [SPAffineTransform3DIsValid](../spaffinetransform3disvalid.md)
  A Boolean value that indicates whether the transform is a valid transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/matrix4x4)*