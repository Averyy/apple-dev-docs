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

#### Discussion

The value of this property must be a two-dimensional path starting at the point `{1, 0}` and ending at the point `{0, 1}`, determining the contour of the shape along its extruded sides. If the value of this property is `nil` and the value of the [`chamferRadius`](./chamferradius.md) property is greater than zero, SceneKit uses a chamfer profile in the shape of a quarter circle. [Figure 1](./api-1523334-chamferprofile.md#1965884) illustrates various chamfer profiles applied to the shape of a tilde (~) character.

![](https://developer.apple.com/tutorials/images/com.apple.scenekit/media-1965884@2x.png)

## See Also

### Managing the Text’s 3D Representation
- [var flatness: CGFloat](./flatness.md)
  A number that determines the accuracy or smoothness of the text geometry.
- [var extrusionDepth: CGFloat](./extrusiondepth.md)
  The extent of the extruded text in the z-axis direction. Animatable.
- [var chamferRadius: CGFloat](./chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/chamferprofile)*