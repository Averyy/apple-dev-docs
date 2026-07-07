# functionConstantInputs

**Framework**: RealityKit  
**Kind**: property

The names of graph inputs whose values are baked in at program compilation time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var functionConstantInputs: [String]
```

#### Discussion

Function constant inputs are compiled directly into the shader and cannot be changed after [`ShaderGraphMaterial.Program`](shadergraphmaterial/program-swift.struct.md) is created. Supply their values via [`constantValues`](shadergraphmaterial/program-swift.struct/descriptor-swift.struct/constantvalues.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/functionconstantinputs)*