# focalLength

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The camera’s focal length, in millimeters.

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
var focalLength: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat focalLength;
```

#### Discussion

The [`sensorHeight`](./sensorheight.md) and [`focalLength`](./focallength.md) properties determine the camera’s horizontal and vertical viewing angles using terms that model physical camera devices. (Alternatively, you can work with viewing angle directly though the [`fieldOfView`](./fieldofview.md) property.) For example, with the default sensor height of 24 mm and default focal length of 50 mm, the vertical field of view is 60°.

Setting the [`fieldOfView`](./fieldofview.md) property causes SceneKit to automatically recalculate the [`focalLength`](./focallength.md) value, and setting the [`sensorHeight`](./sensorheight.md) or [`focalLength`](./focallength.md) property recalculates [`fieldOfView`](./fieldofview.md).

## See Also

### Managing Field of View
- [var fieldOfView: CGFloat](./fieldofview.md)
  The vertical or horizontal viewing angle of the camera.
- [var sensorHeight: CGFloat](./sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](./projectiondirection.md)
  The axis used to determine field of view or orthographic scale.
- [enum SCNCameraProjectionDirection](../scncameraprojectiondirection.md)
  Options for the axis used to determine field of view or orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/focallength)*