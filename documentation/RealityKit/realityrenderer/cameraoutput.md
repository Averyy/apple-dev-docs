# RealityRenderer.CameraOutput

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Output produced by rendering with a camera.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct CameraOutput
```

## Topics

### Structures
- [RealityRenderer.CameraOutput.Descriptor](./cameraoutput/descriptor.md)
  Describes the output of rendering with a camera.
- [RealityRenderer.CameraOutput.RelativeViewport](./cameraoutput/relativeviewport.md)
  Structure defining a viewport for rendering with a camera.
### Initializers
- [init(RealityRenderer.CameraOutput.Descriptor) throws](./cameraoutput/init%28_%29.md)
  Create a new output instance for rendering with a camera.
### Instance Properties
- [var colorTextures: [any MTLTexture]](./cameraoutput/colortextures.md)
  Textures to store color output.
- [var viewports: [RealityRenderer.CameraOutput.RelativeViewport]](./cameraoutput/viewports.md)
  Viewports to use for rendering with a camera.

## See Also

### Metal workflow rendering
- [class RealityRenderer](../realityrenderer.md)
  A renderer that displays a RealityKit scene in an existing Metal workflow.
- [RealityRenderer.CameraSettings](./camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.ImageBasedLight](./imagebasedlight.md)
  Describe the lighting properties for the scene.
- [RealityRenderer.MetalEventAction](./metaleventaction.md)
  The structure describing an event and value to be signaled or waited for.
- [RealityRenderer.EntityCollection](./entitycollection.md)
  A collection of entities in a [`RealityRenderer`](../realityrenderer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/cameraoutput)*