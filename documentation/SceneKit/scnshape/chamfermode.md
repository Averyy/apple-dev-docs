# chamferMode

**Framework**: SceneKit  
**Kind**: property

A constant specifying which ends of the extruded shape’s profile are chamfered.

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
var chamferMode: SCNChamferMode { get set }
```

#### Discussion

See [`SCNChamferMode`](scnchamfermode.md) for allowed values. The default chamfer mode is [`SCNChamferMode.both`](scnchamfermode/both.md).

## See Also

- [enum SCNChamferMode](scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](scnshape/chamfermode.md) property.
- [var chamferProfile: UIBezierPath?](scnshape/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [var chamferRadius: CGFloat](scnshape/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/chamfermode)*