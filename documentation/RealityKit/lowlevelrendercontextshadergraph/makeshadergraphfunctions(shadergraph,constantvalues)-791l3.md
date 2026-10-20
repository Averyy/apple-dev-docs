# makeShaderGraphFunctions(shaderGraph:constantValues:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A synchronous variant of [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](./makeshadergraphfunctions%28shadergraph,constantvalues%29-791l3.md) for non-async callers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) throws -> sending LowLevelMaterialResource.ShaderGraphOutput
```

**Other overloads**:

```swift
nonisolated
(nonsending) func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) async throws -> sending LowLevelMaterialResource.ShaderGraphOutput
```

#### Return Value

The compiled functions for use in a [`LowLevelMaterialResource`](../lowlevelmaterialresource.md).

## Parameters

- `shaderGraph`: The ShaderGraph to compile.
- `constantValues`: The Metal function constant values used to specialize the compiled functions.

## See Also

### Creating shader graph functions
- [func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) async throws -> sending LowLevelMaterialResource.ShaderGraphOutput](./makeshadergraphfunctions%28shadergraph,constantvalues%29-9d8oc.md)
  Compiles a ShaderGraph into a geometry modifier and surface shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:)-791l3)*