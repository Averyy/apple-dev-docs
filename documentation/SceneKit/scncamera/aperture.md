# aperture

**Framework**: SceneKit  
**Kind**: property

A factor that determines the transition between in-focus and out-of-focus areas. Animatable.

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
var aperture: CGFloat { get set }
```

#### Discussion

Objects at distances from the camera outside its depth of field (specified by the [`focalDistance`](scncamera/focaldistance.md) and [`focalSize`](scncamera/focalsize.md) properties) appear increasingly blurred (up to the value of the [`focalBlurRadius`](scncamera/focalblurradius.md) property). Aperture controls the abruptness of the transition between sharp and blurred—a low value specifies an abrupt transition, and a higher value specifies a gradual transition. The default aperture is `0.125` (or 1/8).

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var yFov: Double](scncamera/yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var xFov: Double](scncamera/xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalDistance: CGFloat](scncamera/focaldistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var focalSize: CGFloat](scncamera/focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](scncamera/focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/aperture)*