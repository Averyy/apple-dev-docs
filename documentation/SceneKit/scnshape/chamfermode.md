# chamferMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A constant specifying which ends of the extruded shape’s profile are chamfered.

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
var chamferMode: SCNChamferMode { get set }
```

```objc
@property (nonatomic) SCNChamferMode chamferMode;
```

#### Discussion

See [`SCNChamferMode`](../scnchamfermode.md) for allowed values. The default chamfer mode is [`SCNChamferMode.both`](../scnchamfermode/both.md).

## See Also

### Chamfering a Shape
- [enum SCNChamferMode](../scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](./chamfermode.md) property.
- [var chamferProfile: UIBezierPath?](./chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [var chamferRadius: CGFloat](./chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/chamfermode)*