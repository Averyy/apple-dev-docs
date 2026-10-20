# focalDistance

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The distance from the camera at which objects appear in sharp focus. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use [`focusDistance`](./focusdistance.md) instead.

## Declaration

```swift
var focalDistance: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat focalDistance;
```

#### Discussion

Objects at this distance from the camera appear perfectly focused. Objects nearer to or farther from the camera than this distance appear increasingly blurred (up to the amount of blur specified by the [`focalBlurRadius`](./focalblurradius.md) property). The default focal distance is `10.0`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Deprecated
- [var yFov: Double](./yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var xFov: Double](./xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalSize: CGFloat](./focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](./focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.
- [var aperture: CGFloat](./aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focaldistance)*