# SCNCameraProjectionDirection

**Framework**: SceneKit  
**Kind**: enum

Options for the axis used to determine field of view or orthographic projection.

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
enum SCNCameraProjectionDirection
```

## Topics

### Projection Directions
- [SCNCameraProjectionDirection.vertical](scncameraprojectiondirection/vertical.md)
  The camera’s field of view or orthographic scale are measured vertically.
- [SCNCameraProjectionDirection.horizontal](scncameraprojectiondirection/horizontal.md)
  The camera’s field of view or orthographic scale are measured horizontally.
### Initializers
- [init?(rawValue: Int)](scncameraprojectiondirection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var fieldOfView: CGFloat](scncamera/fieldofview.md)
  The vertical or horizontal viewing angle of the camera.
- [var focalLength: CGFloat](scncamera/focallength.md)
  The camera’s focal length, in millimeters.
- [var sensorHeight: CGFloat](scncamera/sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](scncamera/projectiondirection.md)
  The axis used to determine field of view or orthographic scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameraprojectiondirection)*