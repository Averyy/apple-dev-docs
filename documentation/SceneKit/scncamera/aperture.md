# aperture

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A factor that determines the transition between in-focus and out-of-focus areas. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use [`fStop`](./fstop.md) instead. Note [`fStop`](./fstop.md) `=` [`sensorHeight`](./sensorheight.md) `/` [`aperture`](./aperture.md).

## Declaration

```swift
var aperture: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat aperture;
```

## Discussion

Objects at distances from the camera outside its depth of field (specified by the [`focalDistance`](./focaldistance.md) and [`focalSize`](./focalsize.md) properties) appear increasingly blurred (up to the value of the [`focalBlurRadius`](./focalblurradius.md) property). Aperture controls the abruptness of the transition between sharp and blurred—a low value specifies an abrupt transition, and a higher value specifies a gradual transition. The default aperture is `0.125` (or 1/8).

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
- [var focalBlurRadius: CGFloat](./focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/aperture)*