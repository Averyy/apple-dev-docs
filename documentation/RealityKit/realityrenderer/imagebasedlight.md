# RealityRenderer.ImageBasedLight

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Describe the lighting properties for the scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageBasedLight
```

## Topics

### Instance Properties
- [var intensityExponent: Float](./imagebasedlight/intensityexponent.md)
  The intensity value of the light. The intensity modulates the intensity specified in the diffuse and specular textures An intensity of 0 means using the diffuse/specular intensities as-is Otherwise the intensity is multiplied by 2^intensity
- [var resource: EnvironmentResource?](./imagebasedlight/resource.md)
  The corresponding `EnvironmentResource` used for your Image Based Light.

## See Also

### Metal workflow rendering
- [class RealityRenderer](../realityrenderer.md)
  A renderer that displays a RealityKit scene in an existing Metal workflow.
- [RealityRenderer.CameraSettings](./camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.CameraOutput](./cameraoutput.md)
  Output produced by rendering with a camera.
- [RealityRenderer.MetalEventAction](./metaleventaction.md)
  The structure describing an event and value to be signaled or waited for.
- [RealityRenderer.EntityCollection](./entitycollection.md)
  A collection of entities in a [`RealityRenderer`](../realityrenderer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/imagebasedlight)*