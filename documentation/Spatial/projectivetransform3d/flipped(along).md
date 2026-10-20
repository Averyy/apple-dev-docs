# flipped(along:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a projective transform that results from flipping it along the specified axis.

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
func flipped(along axis: Axis3D) -> ProjectiveTransform3D
```

## Parameters

- `axis`: An axis structure that specifies the flip axis.

## See Also

### Transforming a 3D projective transform structure
- [func sheared(AxisWithFactors) -> ProjectiveTransform3D](./sheared%28_%29.md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [enum AxisWithFactors](../axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](../axis3d.md)
  Constants that describe an axis.
- [func flip(along: Axis3D)](./flip%28along%29.md)
  Flips a projective transform along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/flipped(along:))*