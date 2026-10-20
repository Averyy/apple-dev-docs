# PortalMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Configuration used to compile a [`PortalMaterial.Program`](../program-swift.struct.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(shaderGraph: ShaderGraph, inputValues: [String : MaterialParameters.Value], constantValues: MTLFunctionConstantValues)](./descriptor-swift.struct/init%28shadergraph,inputvalues,constantvalues%29.md)
  Creates a descriptor with the given shader graph and optional initial values.
### Configuring the shader program
- [var shaderGraph: ShaderGraph](./descriptor-swift.struct/shadergraph.md)
  The shader graph that describes the shading logic for this program.
- [var inputValues: [String : MaterialParameters.Value]](./descriptor-swift.struct/inputvalues.md)
  Initial values for the inputs that the shader graph declares.
- [var constantValues: MTLFunctionConstantValues](./descriptor-swift.struct/constantvalues.md)
  Values for the function-constant inputs that the shader graph declares.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)

## See Also

### Configuring the program
- [var descriptor: PortalMaterial.Program.Descriptor](./descriptor-swift.property.md)
  The descriptor that produced this program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct/descriptor-swift.struct)*