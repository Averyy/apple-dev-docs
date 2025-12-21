# controlPointBuffer

**Framework**: Metal  
**Kind**: property

References a buffer containing curve control points.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var controlPointBuffer: MTL4BufferRange { get set }
```

#### Discussion

Control points are interpolated according to the basis function you specify in [`curveBasis`](mtl4accelerationstructurecurvegeometrydescriptor/curvebasis.md).

You are responsible for ensuring each control is in a format matching the control point format [`controlPointFormat`](mtl4accelerationstructurecurvegeometrydescriptor/controlpointformat.md) specifies, as well as ensuring that the buffer address of the range is not zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructurecurvegeometrydescriptor/controlpointbuffer)*