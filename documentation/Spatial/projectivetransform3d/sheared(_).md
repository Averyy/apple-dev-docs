# sheared(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
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

### Transforming a 3D projective transform structure
- [enum AxisWithFactors](../axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](../axis3d.md)
  Constants that describe an axis.
- [func flip(along: Axis3D)](./flip%28along%29.md)
  Flips a projective transform along the specified axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](./flipped%28along%29.md)
  Returns a projective transform that results from flipping it along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/sheared(_:))*