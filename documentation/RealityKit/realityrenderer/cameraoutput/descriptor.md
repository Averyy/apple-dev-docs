# RealityRenderer.CameraOutput.Descriptor

**Framework**: RealityKit  
**Kind**: struct

Describes the output of rendering with a camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Instance Properties
- [var colorTextures: [any MTLTexture]](realityrenderer/cameraoutput/descriptor/colortextures.md)
  Textures to store color output.
- [var viewports: [RealityRenderer.CameraOutput.RelativeViewport]](realityrenderer/cameraoutput/descriptor/viewports.md)
  Viewports to use for rendering with a camera.
### Type Methods
- [static func singleProjection(colorTexture: any MTLTexture) -> RealityRenderer.CameraOutput.Descriptor](realityrenderer/cameraoutput/descriptor/singleprojection(colortexture:).md)
  Creates a descriptor for single projection output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/cameraoutput/descriptor)*