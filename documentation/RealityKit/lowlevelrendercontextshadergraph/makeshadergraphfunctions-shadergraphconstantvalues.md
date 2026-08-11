# makeShaderGraphFunctions(shaderGraph:constantValues:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

A synchronous variant of [`makeShaderGraphFunctions(shaderGraph:constantValues:)`](lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:).md) for non-async callers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeShaderGraphFunctions(shaderGraph: ShaderGraph, constantValues: MTLFunctionConstantValues) throws -> sending LowLevelMaterialResource.ShaderGraphOutput
```

#### Return Value

The compiled functions for use in a [`LowLevelMaterialResource`](lowlevelmaterialresource.md).

## Parameters

- `shaderGraph`: The ShaderGraph to compile.
- `constantValues`: The Metal function constant values used to specialize the compiled functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextshadergraph/makeshadergraphfunctions(shadergraph:constantvalues:))*