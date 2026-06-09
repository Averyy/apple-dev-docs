# LowLevelRenderer.CameraArray

**Framework**: RealityKit  
**Kind**: struct

A mutable, fixed-capacity array of camera values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct CameraArray
```

#### Overview

Set `count` to the number of active cameras before calling `render(using:_:)`.

## Topics

### Creating a camera array
- [init(cameras: [LowLevelRenderer.Camera])](lowlevelrenderer/cameraarray/init(cameras:).md)
  Creates a camera array populated with the given cameras.
### Accessing the camera count
- [var count: Int](lowlevelrenderer/cameraarray/count.md)
  The number of active cameras.
- [static let maxCount: Int](lowlevelrenderer/cameraarray/maxcount.md)
  The maximum number of cameras supported.
### Subscripts
- [subscript(Int) -> LowLevelRenderer.Camera](lowlevelrenderer/cameraarray/subscript(_:).md)
  Returns or sets the camera at the given index.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var cameras: LowLevelRenderer.CameraArray](lowlevelrenderer/cameras.md)
  The array of active cameras.
- [LowLevelRenderer.Camera](lowlevelrenderer/camera.md)
  The view and projection parameters for a single camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cameraarray)*