# isInvertible

**Framework**: Spatial  
**Kind**: property

Returns a Boolean value that indicates whether the transform is invertible.

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
var isInvertible: Bool { get }
```

## See Also

- [struct Dimension3DSet](dimension3dset.md)
  A set of dimensions.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](affinetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var matrix: simd_double4x3](affinetransform3d/matrix.md)
  The affine transform’s underlying matrix.
- [var matrix3x3: simd_double3x3](affinetransform3d/matrix3x3.md)
  The first three columns of an affine transform’s underlying matrix.
- [var matrix4x4: simd_double4x4](affinetransform3d/matrix4x4.md)
  A 4 x 4 matrix that results from constructing the affine transform’s underlying matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/isinvertible)*