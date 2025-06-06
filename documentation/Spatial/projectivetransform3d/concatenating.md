# concatenating(_:)

**Framework**: Spatial  
**Kind**: method

Returns a projective transformation matrix that results from concatenating two existing projective transforms.

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
func concatenating(_ t2: ProjectiveTransform3D) -> ProjectiveTransform3D
```

#### Return Value

The projective transformation matrix that results from concatenating two existing projective transforms.

#### Discussion

This function performs the matrix multiplication `self * t2` on the underlying matrices of the two transforms.

## Parameters

- `t2`: The projective transform that the function concatenates to this projective transform.

## See Also

- [func sheared(AxisWithFactors) -> ProjectiveTransform3D](projectivetransform3d/sheared(_:).md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [func flip(along: Axis3D)](projectivetransform3d/flip(along:).md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](projectivetransform3d/flipped(along:).md)
  Returns a projective transform that results from flipping it along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/concatenating(_:))*