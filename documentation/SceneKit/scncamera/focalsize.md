# focalSize

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The width of the distance range at which objects appear in sharp focus. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use [`focusDistance`](./focusdistance.md) instead; see also [`fStop`](./fstop.md).

## Declaration

```swift
var focalSize: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat focalSize;
```

#### Discussion

The [`focalDistance`](./focaldistance.md) property specifies how far away from the camera an object needs to be to appear in sharp focus. Focal size specifies how wide an area around that distance also appears in sharp focus. The default focus size is `0.0`, specifying that the transition from sharp to blurred begins for objects immediately nearer to or farther from the camera than the focal distance. When focal size is nonzero, it specifies the distance between the nearest an object can be to the camera and remain in sharp focus to the farthest an object can be from the camera and remain in sharp focus.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Deprecated
- [var yFov: Double](./yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var xFov: Double](./xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalDistance: CGFloat](./focaldistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](./focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.
- [var aperture: CGFloat](./aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focalsize)*