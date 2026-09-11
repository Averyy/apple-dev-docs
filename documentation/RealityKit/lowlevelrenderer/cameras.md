# cameras

**Framework**: RealityKit  
**Kind**: property

The array of active cameras.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var cameras: LowLevelRenderer.CameraArray { get set }
```

#### Discussion

Set `cameras.count` to the number of active cameras before calling [`render(using:_:)`](lowlevelrenderer/render(using:_:).md)..

## See Also

- [LowLevelRenderer.CameraArray](lowlevelrenderer/cameraarray.md)
  A mutable, fixed-capacity array of camera values.
- [LowLevelRenderer.Camera](lowlevelrenderer/camera.md)
  The view and projection parameters for a single camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cameras)*