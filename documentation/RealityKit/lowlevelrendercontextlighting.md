# LowLevelRenderContextLighting

**Framework**: RealityKit  
**Kind**: protocol

An entry point for creating lighting functions for use in materials.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol LowLevelRenderContextLighting
```

## Topics

### Making lighting functions
- [func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextlighting/makeimagebasedlightingfunction.md)
  Returns a lighting function using image-based lighting (IBL).
- [func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextlighting/makeunlitlightingfunction.md)
  Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.

## Relationships

### Conforming Types
- [LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown by render context factory methods when resource creation fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown by the renderer during initialization or rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextlighting)*