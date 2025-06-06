# projectionDirection

**Framework**: SceneKit  
**Kind**: property

The axis used to determine field of view or orthographic scale.

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
var projectionDirection: SCNCameraProjectionDirection { get set }
```

#### Discussion

The [`fieldOfView`](scncamera/fieldofview.md) property measures view angle in a single primary direction, determined by this [`projectionDirection`](scncamera/projectiondirection.md) property. For the other direction, SceneKit automatically adjusts field of view depending on the aspect ratio of the view presenting the scene.

For example, with the default projection direction of [`SCNCameraProjectionDirection.vertical`](scncameraprojectiondirection/vertical.md), setting [`fieldOfView`](scncamera/fieldofview.md) to `60` results in a vertical view angle of 60°. If the scene appears on a display with a 4:3 aspect ratio, the horizontal view angle is 80°. However, if the scene appears on a 16:9 display, the horizontal view angle is 106°.

This property has a similar effect on scaling for orthographic projections. The [`orthographicScale`](scncamera/orthographicscale.md) property measures the scale factor in the direction of the [`projectionDirection`](scncamera/projectiondirection.md) property, and SceneKit automatically calculates scale factor in the other direction according to aspect ratio.

## See Also

- [var fieldOfView: CGFloat](scncamera/fieldofview.md)
  The vertical or horizontal viewing angle of the camera.
- [var focalLength: CGFloat](scncamera/focallength.md)
  The camera’s focal length, in millimeters.
- [var sensorHeight: CGFloat](scncamera/sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [enum SCNCameraProjectionDirection](scncameraprojectiondirection.md)
  Options for the axis used to determine field of view or orthographic projection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncamera/projectiondirection)*