# PortalMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct

Configuration used to compile a [`PortalMaterial.Program`](portalmaterial/program-swift.struct.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(shaderGraph: ShaderGraph, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues)](portalmaterial/program-swift.struct/descriptor-swift.struct/init(shadergraph:inputvalues:constantvalues:).md)
  Creates a descriptor with the given shader graph and optional initial values.
### Configuring the shader program
- [var shaderGraph: ShaderGraph](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](portalmaterial/program-swift.struct/descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs declared in [`shaderGraph`](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md).
- [var constantValues: MTLFunctionConstantValues](portalmaterial/program-swift.struct/descriptor-swift.struct/constantvalues.md)
  Values for the function constant inputs declared in [`shaderGraph`](portalmaterial/program-swift.struct/descriptor-swift.struct/shadergraph.md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var descriptor: PortalMaterial.Program.Descriptor](portalmaterial/program-swift.struct/descriptor-swift.property.md)
  The descriptor used to create this program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct)*