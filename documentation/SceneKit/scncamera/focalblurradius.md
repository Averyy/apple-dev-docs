# focalBlurRadius

**Framework**: SceneKit  
**Kind**: property

The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.

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
var focalBlurRadius: CGFloat { get set }
```

#### Discussion

The default value of this property is `0.0`, disabling the depth of field visual effect. Changing this property to a nonzero value enables the depth of field effect, in which only objects at a specified distance from the camera appear in sharp focus, and objects nearer to or farther from the camera appear increasingly blurred (up to the amount specified by this property).

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
- [var aperture: CGFloat](scncamera/aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focalblurradius)*