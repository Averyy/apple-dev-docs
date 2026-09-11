# constantValues

**Framework**: RealityKit  
**Kind**: property

Values for the function constant inputs declared in `shaderNodeGraph`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var constantValues: MTLFunctionConstantValues
```

#### Discussion

Function constants are compiled directly into the shader and cannot be changed after the program is created.

## See Also

- [var shaderGraph: ShaderGraph](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs declared in `shaderNodeGraph`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/program-swift.struct/descriptor-swift.struct/constantvalues)*