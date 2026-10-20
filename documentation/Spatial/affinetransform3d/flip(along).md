# flip(along:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Flips an affine transform along the specified axis.

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
mutating func flip(along axis: Axis3D)
```

## Parameters

- `axis`: An axis structure that specifies the flip axis.

## See Also

### Transforming a 3D affine transform structure
- [struct Axis3D](../axis3d.md)
  Constants that describe an axis.
- [enum AxisWithFactors](../axiswithfactors.md)
  Constants that describe the axis of a shear transform.
- [func changeBasis(from: AffineTransform3D, to: AffineTransform3D) -> AffineTransform3D?](./changebasis%28from,to%29.md)
  Returns a new affine transform structure by applying a change-of-basis.
- [func flipped(along: Axis3D) -> AffineTransform3D](./flipped%28along%29.md)
  Returns an affine transform that results from flipping it along the specified axis.
- [var inverse: AffineTransform3D?](./inverse.md)
  The affine transform’s inverse.
- [func scaledBy(x: Double, y: Double, z: Double) -> AffineTransform3D](./scaledby%28x,y,z%29.md)
  Returns a transform that results from scaling with specified double-precision values.
- [func sheared(AxisWithFactors) -> AffineTransform3D](./sheared%28_%29.md)
  Returns an affine transform that results from shearing over an axis by shear factors for the other two axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/affinetransform3d/flip(along:))*