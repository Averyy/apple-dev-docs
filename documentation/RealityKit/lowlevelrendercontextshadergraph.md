# LowLevelRenderContextShaderGraph

**Framework**: RealityKit  
**Kind**: protocol

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol LowLevelRenderContextShaderGraph
```

## Topics

### Creating shader graph functions
- [func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) throws -> sending LowLevelMaterialResource.ShaderGraphOutput](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-791l3.md)
- [func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) async throws -> sending LowLevelMaterialResource.ShaderGraphOutput](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-9d8oc.md)
### Instance Methods
- [func makeShaderGraphFunctions(shaderGraph:constantValues:)](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:).md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  An entry point for creating lighting functions for use in materials.
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown by render context factory methods when resource creation fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown by the renderer during initialization or rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextshadergraph)*