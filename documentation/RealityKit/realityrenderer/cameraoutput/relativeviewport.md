# RealityRenderer.CameraOutput.RelativeViewport

**Framework**: RealityKit  
**Kind**: struct

Structure defining a viewport for rendering with a camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct RelativeViewport
```

#### Overview

The units are relative to output texture size. To map normalized-device coordinates to the whole texture:

```swift
viewport = RealityRenderer.CameraOutput.RelativeViewport(originX: 0.0, originY: 0.0, width: 1.0, height: 1.0)
```

Assigning values more than 1.0 to [`width`](realityrenderer/cameraoutput/relativeviewport/width.md) or [`height`](realityrenderer/cameraoutput/relativeviewport/height.md) stretches the viewport in horizontal and vertical directions.

Assigning values less than 0.0 to [`originX`](realityrenderer/cameraoutput/relativeviewport/originx.md) or [`originY`](realityrenderer/cameraoutput/relativeviewport/originy.md) shifts the viewport into negative X and negative Y directions.

## Topics

### Initializers
- [init(originX: Double, originY: Double, width: Double, height: Double)](realityrenderer/cameraoutput/relativeviewport/init(originx:originy:width:height:).md)
### Instance Properties
- [var height: Double](realityrenderer/cameraoutput/relativeviewport/height.md)
- [var originX: Double](realityrenderer/cameraoutput/relativeviewport/originx.md)
- [var originY: Double](realityrenderer/cameraoutput/relativeviewport/originy.md)
- [var width: Double](realityrenderer/cameraoutput/relativeviewport/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/cameraoutput/relativeviewport)*