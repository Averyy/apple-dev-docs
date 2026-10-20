# SCNCameraProjectionDirection

**Framework**: SceneKit  
**Kind**: enum  
**Role**: Enumeration

Options for the axis used to determine field of view or orthographic projection.

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
enum SCNCameraProjectionDirection
```

```c
enum SCNCameraProjectionDirection : NSInteger;
```

## Topics

### Projection Directions
- [SCNCameraProjectionDirection.vertical](./scncameraprojectiondirection/vertical.md)
  The camera’s field of view or orthographic scale are measured vertically.
- [SCNCameraProjectionDirection.horizontal](./scncameraprojectiondirection/horizontal.md)
  The camera’s field of view or orthographic scale are measured horizontally.
### Initializers
- [init?(rawValue: Int)](./scncameraprojectiondirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Field of View
- [var fieldOfView: CGFloat](./scncamera/fieldofview.md)
  The vertical or horizontal viewing angle of the camera.
- [var focalLength: CGFloat](./scncamera/focallength.md)
  The camera’s focal length, in millimeters.
- [var sensorHeight: CGFloat](./scncamera/sensorheight.md)
  The vertical size of the camera’s imaging plane, in millimeters.
- [var projectionDirection: SCNCameraProjectionDirection](./scncamera/projectiondirection.md)
  The axis used to determine field of view or orthographic scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncameraprojectiondirection)*