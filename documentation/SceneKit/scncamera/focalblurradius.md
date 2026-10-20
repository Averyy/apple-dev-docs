# focalBlurRadius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use [`fStop`](./fstop.md) instead to define physically based variable blur effects instead of a constant radius. (Note [`fStop`](./fstop.md) `=` [`sensorHeight`](./sensorheight.md) `/` [`aperture`](./aperture.md).)

## Declaration

```swift
var focalBlurRadius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat focalBlurRadius;
```

#### Discussion

The default value of this property is `0.0`, disabling the depth of field visual effect. Changing this property to a nonzero value enables the depth of field effect, in which only objects at a specified distance from the camera appear in sharp focus, and objects nearer to or farther from the camera appear increasingly blurred (up to the amount specified by this property).

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Deprecated
- [var yFov: Double](./yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var xFov: Double](./xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalDistance: CGFloat](./focaldistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var focalSize: CGFloat](./focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var aperture: CGFloat](./aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focalblurradius)*