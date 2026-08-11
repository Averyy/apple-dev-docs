# LowLevelRenderContextShaderGraph

**Framework**: RealityKit  
**Kind**: protocol

The interface for creating Metal shader functions from a ShaderGraph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol LowLevelRenderContextShaderGraph
```

#### Overview

Access this through [`shaderGraph`](lowlevelrendercontext/shadergraph.md).

## Topics

### Creating shader graph functions
- [func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) throws -> sending LowLevelMaterialResource.ShaderGraphOutput](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-791l3.md)
  A synchronous variant of [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-791l3.md) for non-async callers.
- [func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) async throws -> sending LowLevelMaterialResource.ShaderGraphOutput](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-9d8oc.md)
  Compiles a ShaderGraph into a geometry modifier and surface shader.
### Instance Methods
- [func makeShaderGraphFunctions(shaderGraph:constantValues:)](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:).md)
  A synchronous variant of [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:).md) for non-async callers.

## Relationships

### Conforming Types
- [LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  The interface for creating lighting functions for use in materials.
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown when binding or updating a low-level rendering resource fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown when creating or configuring a renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextshadergraph)*