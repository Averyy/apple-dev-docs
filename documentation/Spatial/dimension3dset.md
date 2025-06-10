# Dimension3DSet

**Framework**: Spatial  
**Kind**: struct

A set of dimensions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct Dimension3DSet
```

## Topics

### Type properties
- [static let all: Dimension3DSet](dimension3dset/all.md)
  All dimensions.
- [static let x: Dimension3DSet](dimension3dset/x.md)
  The x-dimension.
- [static let y: Dimension3DSet](dimension3dset/y.md)
  The y-dimension.
- [static let z: Dimension3DSet](dimension3dset/z.md)
  The z-dimension.
### Instance properties
- [let rawValue: Int](dimension3dset/rawvalue.md)
  The corresponding value of the raw type.
### Initializers
- [init(rawValue: Int)](dimension3dset/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var isInvertible: Bool](affinetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](affinetransform3d/isuniform(overdimensions:).md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var matrix: simd_double4x3](affinetransform3d/matrix.md)
  The affine transform’s underlying matrix.
- [var matrix3x3: simd_double3x3](affinetransform3d/matrix3x3.md)
  The first three columns of an affine transform’s underlying matrix.
- [var matrix4x4: simd_double4x4](affinetransform3d/matrix4x4.md)
  A 4 x 4 matrix that results from constructing the affine transform’s underlying matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/dimension3dset)*