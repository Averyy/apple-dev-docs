# sheared(_:)

**Framework**: Spatial  
**Kind**: method

Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.

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
func sheared(_ shear: AxisWithFactors) -> ProjectiveTransform3D
```

#### Return Value

The projective transform that results from shearing over an axis by shear factors for the other two axes.

## Parameters

- `shear`: The shear axis and factors.

## See Also

- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [func concatenating(ProjectiveTransform3D) -> ProjectiveTransform3D](projectivetransform3d/concatenating(_:).md)
  Returns a projective transformation matrix that results from concatenating two existing projective transforms.
- [func flip(along: Axis3D)](projectivetransform3d/flip(along:).md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](projectivetransform3d/flipped(along:).md)
  Returns a projective transform that results from flipping it along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/sheared(_:))*