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

- `shaderGraph`: The shader graph that describes the program’s surface and, optionally, geometry-modifier shading.
- `inputValues`: Initial values for the inputs the shader graph declares. Defaults to an empty dictionary, leaving each input at its declared default.
- `constantValues`: Values for the function-constant inputs the shader graph declares. Defaults to an empty `MTLFunctionConstantValues`, leaving each function constant at its declared default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct/init(shadergraph:inputvalues:constantvalues:))*