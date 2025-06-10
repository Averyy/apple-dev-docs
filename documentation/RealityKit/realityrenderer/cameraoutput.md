# RealityRenderer.CameraOutput

**Framework**: RealityKit  
**Kind**: struct

Output produced by rendering with a camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct CameraOutput
```

## Topics

### Structures
- [RealityRenderer.CameraOutput.Descriptor](realityrenderer/cameraoutput/descriptor.md)
  Describes the output of rendering with a camera.
- [RealityRenderer.CameraOutput.RelativeViewport](realityrenderer/cameraoutput/relativeviewport.md)
  Structure defining a viewport for rendering with a camera.
### Initializers
- [init(RealityRenderer.CameraOutput.Descriptor) throws](realityrenderer/cameraoutput/init(_:).md)
  Create a new output instance for rendering with a camera.
### Instance Properties
- [var colorTextures: [any MTLTexture]](realityrenderer/cameraoutput/colortextures.md)
  Textures to store color output.
- [var viewports: [RealityRenderer.CameraOutput.RelativeViewport]](realityrenderer/cameraoutput/viewports.md)
  Viewports to use for rendering with a camera.

## See Also

- [class RealityRenderer](realityrenderer.md)
  A renderer that displays a RealityKit scene in an existing Metal workflow.
- [RealityRenderer.CameraSettings](realityrenderer/camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.ImageBasedLight](realityrenderer/imagebasedlight.md)
  Describe the lighting properties for the scene.
- [RealityRenderer.MetalEventAction](realityrenderer/metaleventaction.md)
  The structure describing an event and value to be signaled or waited for.
- [RealityRenderer.EntityCollection](realityrenderer/entitycollection.md)
  A collection of entities in a [`RealityRenderer`](realityrenderer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/cameraoutput)*