# focalDistance

**Framework**: SceneKit  
**Kind**: property

The distance from the camera at which objects appear in sharp focus. Animatable.

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
var focalDistance: CGFloat { get set }
```

#### Discussion

Objects at this distance from the camera appear perfectly focused. Objects nearer to or farther from the camera than this distance appear increasingly blurred (up to the amount of blur specified by the [`focalBlurRadius`](scncamera/focalblurradius.md) property). The default focal distance is `10.0`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var yFov: Double](scncamera/yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var xFov: Double](scncamera/xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalSize: CGFloat](scncamera/focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](scncamera/focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.
- [var aperture: CGFloat](scncamera/aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focaldistance)*