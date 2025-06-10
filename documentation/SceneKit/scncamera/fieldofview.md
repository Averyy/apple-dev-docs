# fieldOfView

**Framework**: SceneKit  
**Kind**: property

The vertical or horizontal viewing angle of the camera.

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
var fieldOfView: CGFloat { get set }
```

#### Discussion

The [`projectionDirection`](scncamera/projectiondirection.md) property determines whether this [`fieldOfView`](scncamera/fieldofview.md) property measures the camera’s vertical or horizontal viewing angle, and SceneKit automatically calculates the viewing angle in the other direction to match the aspect ratio of the view displaying the scene. For example, a [`fieldOfView`](scncamera/fieldofview.md) of `60` and the default [`SCNCameraProjectionDirection.vertical`](scncameraprojectiondirection/vertical.md) projection, presented fullscreen on a 16:9 display in portrait orientation, results in a vertical viewing angle of 60° and a horizontal viewing angle of 33.75°.

You can choose to specify viewing angle either directly, using this [`fieldOfView`](scncamera/fieldofview.md) property, or in terms that model a physical camera, using the [`sensorHeight`](scncamera/sensorheight.md) and [`focalLength`](scncamera/focallength.md) properties. Setting the [`fieldOfView`](scncamera/fieldofview.md) property causes SceneKit to automatically recalculate the [`focalLength`](scncamera/focallength.md) value, and setting the [`sensorHeight`](scncamera/sensorheight.md) or [`focalLength`](scncamera/focallength.md) property recalculates [`fieldOfView`](scncamera/fieldofview.md).

## See Also

- [var focalLength: CGFloat](scncamera/focallength.md)
  The camera’s focal length, in millimeters.
- [var sensorHeight: CGFloat](scncamera/sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](scncamera/projectiondirection.md)
  The axis used to determine field of view or orthographic scale.
- [enum SCNCameraProjectionDirection](scncameraprojectiondirection.md)
  Options for the axis used to determine field of view or orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/fieldofview)*