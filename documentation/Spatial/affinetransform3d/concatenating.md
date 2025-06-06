# concatenating(_:)

**Framework**: Spatial  
**Kind**: method

Returns an affine transformation matrix that results from concatenating two existing affine transforms.

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
func concatenating(_ t2: AffineTransform3D) -> AffineTransform3D
```

#### Return Value

The affine transformation matrix that results from concatenating two existing affine transforms.

#### Discussion

This function performs the matrix multiplication `self * t2` on the underlying matrices of the two transforms.

## Parameters

- `t2`: The affine transform that the function concatenates to this affine transform.

## See Also

- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [func changeBasis(from: AffineTransform3D, to: AffineTransform3D) -> AffineTransform3D?](affinetransform3d/changebasis(from:to:).md)
  Returns a new affine transform structure by applying a change-of-basis.
- [func flip(along: Axis3D)](affinetransform3d/flip(along:).md)
  Flips an affine transform along the specified axis.
- [func flipped(along: Axis3D) -> AffineTransform3D](affinetransform3d/flipped(along:).md)
  Returns an affine transform that results from flipping it along the specified axis.
- [var inverse: AffineTransform3D?](affinetransform3d/inverse.md)
  The affine transform’s inverse.
- [func scaledBy(x: Double, y: Double, z: Double) -> AffineTransform3D](affinetransform3d/scaledby(x:y:z:).md)
  Returns a transform that results from scaling with specified double-precision values.
- [func sheared(AxisWithFactors) -> AffineTransform3D](affinetransform3d/sheared(_:).md)
  Returns an affine transform that results from shearing over an axis by shear factors for the other two axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/concatenating(_:))*