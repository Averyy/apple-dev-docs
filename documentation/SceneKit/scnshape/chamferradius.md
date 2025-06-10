# chamferRadius

**Framework**: SceneKit  
**Kind**: property

The width or depth of each chamfered edge. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var chamferRadius: CGFloat { get set }
```

#### Discussion

The default value of zero specifies no chamfer (the extruded sides end at right angles to the front and back of the shape). Allowed values range from zero to half the extrusion depth. (At the maximum chamfer radius, the front chamfer ends where the back chamfer begins, as shown on the right in the figure below.)

![None](https://docs-assets.developer.apple.com/published/22a6025b1c4360a184d188ef3eed788c/media-2929772%402x.png)

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var chamferMode: SCNChamferMode](scnshape/chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [enum SCNChamferMode](scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](scnshape/chamfermode.md) property.
- [var chamferProfile: UIBezierPath?](scnshape/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/chamferradius)*