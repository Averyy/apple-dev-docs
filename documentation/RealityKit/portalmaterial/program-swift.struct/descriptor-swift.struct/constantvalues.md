# constantValues

**Framework**: RealityKit  
**Kind**: property

Values for the function constant inputs declared in [`shaderGraph`](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var constantValues: MTLFunctionConstantValues
```

#### Discussion

Function constants are compiled directly into the shader and cannot be changed after the program is created.

## See Also

- [var shaderGraph: ShaderGraph](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](portalmaterial/program-swift.struct/descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs declared in [`shaderGraph`](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct/constantvalues)*