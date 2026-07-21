# LowLevelRenderContextStandalone

**Framework**: RealityKit  
**Kind**: class

A standalone Metal-backed render context for creating low-level rendering resources.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelRenderContextStandalone
```

#### Overview

`LowLevelRenderContextStandalone` is a concrete implementation of [`LowLevelRenderContext`](lowlevelrendercontext.md) and [`LowLevelRenderContextLighting`](lowlevelrendercontextlighting.md). Create one using the async initializer for full setup including shader and pipeline compilation, or the synchronous initializer using a pre-compiled [`LowLevelRenderContextStandalone.Resources`](lowlevelrendercontextstandalone/resources.md) instance.

## Topics

### Creating a render context
- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](lowlevelrendercontextstandalone/init(configuration:resources:).md)
  Creates a standalone render context using pre-compiled shader and pipeline resources.
- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](lowlevelrendercontextstandalone/init(configuration:).md)
  Creates a standalone render context, asynchronously compiling all required shader and pipeline resources.
- [LowLevelRenderContextStandalone.Configuration](lowlevelrendercontextstandalone/configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.
- [LowLevelRenderContextStandalone.Resources](lowlevelrendercontextstandalone/resources.md)
  Pre-compiled shader and pipeline resources shared across multiple render context instances.
### Creating lighting functions
- [func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextstandalone/makeimagebasedlightingfunction.md)
  Returns a lighting function using image-based lighting (IBL).
- [func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextstandalone/makeunlitlightingfunction.md)
  Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.
### Default Implementations
- [LowLevelRenderContextLighting Implementations](lowlevelrendercontextstandalone/lowlevelrendercontextlighting-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [LowLevelRenderContext](lowlevelrendercontext.md)
- [LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
- [LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  An entry point for creating lighting functions for use in materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown by render context factory methods when resource creation fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown by the renderer during initialization or rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone)*