# yFov

**Framework**: SceneKit  
**Kind**: property

The camera’s field of view, in degrees, on the vertical axis. Animatable.

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
var yFov: Double { get set }
```

#### Discussion

Field of view is an angle that determines the extent of the scene visible to the camera, similar to that of a real-world camera lens. A small field of view angle provides a narrow view, and a large field of view provides a wide view. A very wide field of view results in distorted perspective.

SceneKit allows horizontal and vertical field of view to be set independently. By default, both the [`xFov`](scncamera/xfov.md) and [`yFov`](scncamera/yfov.md) properties are zero, causing SceneKit to use a 60° vertical field of view and automatically adjust the horizontal field of view to fit the renderer’s aspect ratio without distorting the image. If you set only one of the field of view properties to a nonzero value, SceneKit uses that value for its axis and automatically adjusts the field of view in the other axis. If you set both properties, SceneKit uses the property that best fits the renderer’s current aspect ratio and automatically adjusts the field of view in the other axis.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var xFov: Double](scncamera/xfov.md)
  The camera’s field of view, in degrees, on the horizontal axis. Animatable.
- [var focalDistance: CGFloat](scncamera/focaldistance.md)
  The distance from the camera at which objects appear in sharp focus. Animatable.
- [var focalSize: CGFloat](scncamera/focalsize.md)
  The width of the distance range at which objects appear in sharp focus. Animatable.
- [var focalBlurRadius: CGFloat](scncamera/focalblurradius.md)
  The maximum amount of blurring, in pixels, applied to areas outside the camera’s depth of field. Animatable.
- [var aperture: CGFloat](scncamera/aperture.md)
  A factor that determines the transition between in-focus and out-of-focus areas. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/yfov)*