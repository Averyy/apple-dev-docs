# makeShaderGraphFunctions(shaderGraph:constantValues:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Compiles a ShaderGraph into a geometry modifier and surface shader.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) async throws -> sending LowLevelMaterialResource.ShaderGraphOutput
```

#### Return Value

The compiled functions for use in a [`LowLevelMaterialResource`](lowlevelmaterialresource.md).

## Parameters

- `shaderGraph`: The ShaderGraph to compile.
- `constantValues`: The Metal function constant values used to specialize the compiled functions.

## See Also

- [func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) throws -> sending LowLevelMaterialResource.ShaderGraphOutput](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-791l3.md)
  A synchronous variant of [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-791l3.md) for non-async callers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-9d8oc)*