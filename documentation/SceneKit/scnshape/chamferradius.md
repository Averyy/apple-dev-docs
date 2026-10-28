# chamferRadius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The width or depth of each chamfered edge. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var chamferRadius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat chamferRadius;
```

## Discussion

The default value of zero specifies no chamfer (the extruded sides end at right angles to the front and back of the shape). Allowed values range from zero to half the extrusion depth. (At the maximum chamfer radius, the front chamfer ends where the back chamfer begins, as shown on the right in the figure below.)

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929772@2x.png)

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Chamfering a Shape
- [var chamferMode: SCNChamferMode](./chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [enum SCNChamferMode](../scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](./chamfermode.md) property.
- [var chamferProfile: UIBezierPath?](./chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/chamferradius)*