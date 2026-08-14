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

`LowLevelRenderContextStandalone` is a concrete implementation of [`LowLevelRenderContext`](lowlevelrendercontext.md), [`LowLevelRenderContextLighting`](lowlevelrendercontextlighting.md), and [`LowLevelRenderContextShaderGraph`](lowlevelrendercontextshadergraph.md). Create one using [`init(configuration:)`](lowlevelrendercontextstandalone/init(configuration:).md) , or [`init(configuration:resources:)`](lowlevelrendercontextstandalone/init(configuration:resources:).md) with a prepared [`LowLevelRenderContextStandalone.Resources`](lowlevelrendercontextstandalone/resources.md) instance.

## Topics

### Creating a render context
- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](lowlevelrendercontextstandalone/init(configuration:resources:).md)
  Creates a standalone render context using resources prepared ahead of time.
- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](lowlevelrendercontextstandalone/init(configuration:).md)
  Creates a standalone render context, asynchronously preparing required resources.
- [LowLevelRenderContextStandalone.Configuration](lowlevelrendercontextstandalone/configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.
- [LowLevelRenderContextStandalone.Resources](lowlevelrendercontextstandalone/resources.md)
  Resources needed for a render context
### Creating lighting functions
- [func makeImageBasedLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextstandalone/makeimagebasedlightingfunction.md)
  Returns a lighting function using image-based lighting (IBL).
- [func makeUnlitLightingFunction() -> sending LowLevelMaterialResource.LightingFunction](lowlevelrendercontextstandalone/makeunlitlightingfunction.md)
  Returns an unlit lighting function that emits the surface emissive color directly, without any lighting calculations.
### Default Implementations
- [LowLevelRenderContext Implementations](lowlevelrendercontextstandalone/lowlevelrendercontext-implementations.md)
- [LowLevelRenderContextLighting Implementations](lowlevelrendercontextstandalone/lowlevelrendercontextlighting-implementations.md)
- [LowLevelRenderContextShaderGraph Implementations](lowlevelrendercontextstandalone/lowlevelrendercontextshadergraph-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [LowLevelRenderContext](lowlevelrendercontext.md)
- [LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
- [LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  The interface for creating lighting functions for use in materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
  The interface for creating Metal shader functions from a ShaderGraph.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown when binding or updating a low-level rendering resource fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown when creating or configuring a renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone)*