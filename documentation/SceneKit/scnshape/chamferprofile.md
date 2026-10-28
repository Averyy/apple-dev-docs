# chamferProfile

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A path that determines the cross-sectional contour of each chamfered edge.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
@NSCopying
var chamferProfile: UIBezierPath? { get set }
```

*macOS*

```swift
@NSCopying
var chamferProfile: NSBezierPath? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) UIBezierPath * chamferProfile;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSBezierPath * chamferProfile;
```

## Discussion

The value of this property must be a two-dimensional path starting at the point `{1, 0}` and ending at the point `{0, 1}`, determining the contour of the shape along its extruded sides, as illustrated in the figure below. If the value of this property is `nil` and the value of the [`chamferRadius`](./chamferradius.md) property is greater than zero, SceneKit uses a chamfer profile in the shape of a quarter circle.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-2929770@2x.png)

## See Also

### Chamfering a Shape
- [var chamferMode: SCNChamferMode](./chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [enum SCNChamferMode](../scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](./chamfermode.md) property.
- [var chamferRadius: CGFloat](./chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/chamferprofile)*