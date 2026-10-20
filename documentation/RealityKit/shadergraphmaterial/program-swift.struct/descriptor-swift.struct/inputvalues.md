# inputValues

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Initial values for the inputs declared in `shaderNodeGraph`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var inputValues: [String : MaterialParameters.Value]
```

## See Also

### Specifying the shader graph
- [var shaderGraph: ShaderGraph](./shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var constantValues: MTLFunctionConstantValues](./constantvalues.md)
  Values for the function constant inputs declared in `shaderNodeGraph`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct/inputvalues)*