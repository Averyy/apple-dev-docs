# init(shaderGraph:inputValues:constantValues:)

**Framework**: RealityKit  
**Kind**: init

Creates a descriptor with the given shader graph and optional initial values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(shaderGraph: ShaderGraph, inputValues: [String : MaterialParameters.Value] = [:], constantValues: MTLFunctionConstantValues = .init())
```

## Parameters

- `shaderGraph`: The shader graph describing the shading logic for this program.
- `inputValues`: Initial values for the inputs declared in the shader graph.
- `constantValues`: Values for function constant inputs to be baked into the compiled shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct/init(shadergraph:inputvalues:constantvalues:))*