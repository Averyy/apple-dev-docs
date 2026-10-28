# LowLevelRenderer.CameraArray

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A mutable, fixed-capacity array of camera values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct CameraArray
```

## Overview

Set `count` to the number of active cameras before calling [`render(using:_:)`](./render%28using,_%29.md).

## Topics

### Creating a camera array
- [init(cameras: [LowLevelRenderer.Camera])](./cameraarray/init%28cameras%29.md)
  Creates a camera array populated with the given cameras.
### Accessing the camera count
- [var count: Int](./cameraarray/count.md)
  The number of active cameras.
- [static let maxCount: Int](./cameraarray/maxcount.md)
  The maximum number of cameras supported.
### Subscripts
- [subscript(Int) -> LowLevelRenderer.Camera](./cameraarray/subscript%28_%29.md)
  Returns or sets the camera at the given index.

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Configuring cameras
- [var cameras: LowLevelRenderer.CameraArray](./cameras.md)
  The array of active cameras.
- [LowLevelRenderer.Camera](./camera.md)
  The view and projection parameters for a single camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cameraarray)*