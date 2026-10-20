# fieldOfView

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The vertical or horizontal viewing angle of the camera.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var fieldOfView: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat fieldOfView;
```

#### Discussion

The [`projectionDirection`](./projectiondirection.md) property determines whether this [`fieldOfView`](./fieldofview.md) property measures the camera’s vertical or horizontal viewing angle, and SceneKit automatically calculates the viewing angle in the other direction to match the aspect ratio of the view displaying the scene. For example, a [`fieldOfView`](./fieldofview.md) of `60` and the default [`SCNCameraProjectionDirection.vertical`](../scncameraprojectiondirection/vertical.md) projection, presented fullscreen on a 16:9 display in portrait orientation, results in a vertical viewing angle of 60° and a horizontal viewing angle of 33.75°.

You can choose to specify viewing angle either directly, using this [`fieldOfView`](./fieldofview.md) property, or in terms that model a physical camera, using the [`sensorHeight`](./sensorheight.md) and [`focalLength`](./focallength.md) properties. Setting the [`fieldOfView`](./fieldofview.md) property causes SceneKit to automatically recalculate the [`focalLength`](./focallength.md) value, and setting the [`sensorHeight`](./sensorheight.md) or [`focalLength`](./focallength.md) property recalculates [`fieldOfView`](./fieldofview.md).

## See Also

### Managing Field of View
- [var focalLength: CGFloat](./focallength.md)
  The camera’s focal length, in millimeters.
- [var sensorHeight: CGFloat](./sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](./projectiondirection.md)
  The axis used to determine field of view or orthographic scale.
- [enum SCNCameraProjectionDirection](../scncameraprojectiondirection.md)
  Options for the axis used to determine field of view or orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/fieldofview)*