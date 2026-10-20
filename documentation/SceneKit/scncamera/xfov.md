# xFov

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The camera’s field of view, in degrees, on the horizontal axis. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use [`fieldOfView`](./fieldofview.md) instead; see also [`projectionDirection`](./projectiondirection.md).

## Declaration

```swift
var xFov: Double { get set }
```

```objc
@property (nonatomic) double xFov;
```

#### Discussion

Field of view is an angle that determines the extent of the scene visible to the camera, similar to that of a real-world camera lens. A small field of view angle provides a narrow view, and a large field of view provides a wide view. A very wide field of view results in distorted perspective.

SceneKit allows horizontal and vertical field of view to be set independently. By default, both the [`xFov`](./xfov.md) and [`yFov`](./yfov.md) properties are zero, causing SceneKit to use a 60° vertical field of view and automatically adjust the horizontal field of view to fit the renderer’s aspect ratio without distorting the image. If you set only one of the field of view properties to a nonzero value, SceneKit uses that value for its axis and automatically adjusts the field of view in the other axis. If you set both properties, SceneKit uses the property that best fits the renderer’s current aspect ratio and automatically adjusts the field of view in the other axis.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Deprecated
- [var yFov: Double](./yfov.md)
  The camera’s field of view, in degrees, on the vertical axis. Animatable.
- [var focalDistance: CGFloat](./focaldistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var focalSize: CGFloat](./focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](./focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.
- [var aperture: CGFloat](./aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/xfov)*