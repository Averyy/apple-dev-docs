# makeShaderGraphFunctions(shaderGraph:constantValues:)

**Framework**: RealityKit  
**Kind**: method

Compiles a ShaderGraph into a geometry modifier and surface shader.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) final func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) async throws -> sending LowLevelMaterialResource.ShaderGraphOutput
```

#### Return Value

The compiled functions for use in a [`LowLevelMaterialResource`](lowlevelmaterialresource.md).

## Parameters

- `shaderGraph`: The ShaderGraph to compile.
- `constantValues`: The Metal function constant values used to specialize the compiled functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makeshadergraphfunctions(shadergraph:constantvalues:)-7p4ye)*