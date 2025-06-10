# flip(along:)

**Framework**: Spatial  
**Kind**: method

Flips a projective transform along the specified axis.

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
mutating func flip(along axis: Axis3D)
```

## Parameters

- `axis`: An axis structure that specifies the flip axis.

## See Also

- [func sheared(AxisWithFactors) -> ProjectiveTransform3D](projectivetransform3d/sheared(_:).md)
  Returns a projective transform that results from shearing over an axis by shear factors for the other two axes.
- [enum AxisWithFactors](axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [struct Axis3D](axis3d.md)
  Constants that describe an axis.
- [func flipped(along: Axis3D) -> ProjectiveTransform3D](projectivetransform3d/flipped(along:).md)
  Returns a projective transform that results from flipping it along the specified axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/flip(along:))*