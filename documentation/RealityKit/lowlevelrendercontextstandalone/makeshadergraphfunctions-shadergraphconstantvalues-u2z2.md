# makeShaderGraphFunctions(shaderGraph:constantValues:)

**Framework**: RealityKit  
**Kind**: method

A synchronous variant of [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](lowlevelrendercontextstandalone/makeshadergraphfunctions(shadergraph:constantvalues:)-u2z2.md) for non-async callers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) throws -> sending LowLevelMaterialResource.ShaderGraphOutput
```

#### Return Value

The compiled functions for use in a [`LowLevelMaterialResource`](lowlevelmaterialresource.md).

## Parameters

- `shaderGraph`: The ShaderGraph to compile.
- `constantValues`: The Metal function constant values used to specialize the compiled functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makeshadergraphfunctions(shadergraph:constantvalues:)-u2z2)*