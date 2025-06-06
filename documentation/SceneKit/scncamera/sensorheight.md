# sensorHeight

**Framework**: SceneKit  
**Kind**: property

The vertical size of the camera’s imaging plane, in millimeters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var sensorHeight: CGFloat { get set }
```

#### Discussion

The [`sensorHeight`](scncamera/sensorheight.md) and [`focalLength`](scncamera/focallength.md) properties determine the camera’s horizontal and vertical viewing angles using terms that model physical camera devices. (Alternatively, you can work with viewing angle directly though the [`fieldOfView`](scncamera/fieldofview.md) property.) For example, with the default sensor height of 24 mm and default focal length of 50 mm, the vertical field of view is 60°.

Setting the [`fieldOfView`](scncamera/fieldofview.md) property causes SceneKit to automatically recalculate the [`focalLength`](scncamera/focallength.md) value, and setting the [`sensorHeight`](scncamera/sensorheight.md) or [`focalLength`](scncamera/focallength.md) property recalculates [`fieldOfView`](scncamera/fieldofview.md).

## See Also

- [var fieldOfView: CGFloat](scncamera/fieldofview.md)
  The vertical or horizontal viewing angle of the camera.
- [var focalLength: CGFloat](scncamera/focallength.md)
  The camera’s focal length, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](scncamera/projectiondirection.md)
  The axis used to determine field of view or orthographic scale.
- [enum SCNCameraProjectionDirection](scncameraprojectiondirection.md)
  Options for the axis used to determine field of view or orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/sensorheight)*