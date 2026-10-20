# cameras

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

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

Set `cameras.count` to the number of active cameras before calling [`render(using:_:)`](./render%28using,_%29.md)..

## See Also

### Configuring cameras
- [LowLevelRenderer.CameraArray](./cameraarray.md)
  A mutable, fixed-capacity array of camera values.
- [LowLevelRenderer.Camera](./camera.md)
  The view and projection parameters for a single camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/cameras)*