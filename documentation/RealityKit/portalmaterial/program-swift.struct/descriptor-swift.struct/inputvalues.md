# inputValues

**Framework**: RealityKit  
**Kind**: property

Initial values for the inputs that the shader graph declares.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var inputValues: [String : MaterialParameters.Value]
```

#### Discussion

Each entry binds a graph input by name to a starting value. The engine applies these values when a [`PortalMaterial`](portalmaterial.md) is first created from the resulting program; you can change any of them at runtime by calling [`setParameter(name:value:)`](portalmaterial/setparameter(name:value:).md).

Inputs that the graph declares as function constants belong in [`constantValues`](portalmaterial/program-swift.struct/descriptor-swift.struct/constantvalues.md) instead.

## See Also

- [var shaderGraph: ShaderGraph](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var constantValues: MTLFunctionConstantValues](portalmaterial/program-swift.struct/descriptor-swift.struct/constantvalues.md)
  Values for the function-constant inputs that the shader graph declares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct/inputvalues)*