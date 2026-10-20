# PortalMaterial.Program

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A compiled shader program that drives the appearance of a portal’s surface and geometry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Program
```

## Topics

### Configuring the program
- [var descriptor: PortalMaterial.Program.Descriptor](./program-swift.struct/descriptor-swift.property.md)
  The descriptor that produced this program.
- [PortalMaterial.Program.Descriptor](./program-swift.struct/descriptor-swift.struct.md)
  Configuration used to compile a [`PortalMaterial.Program`](./program-swift.struct.md).
### Initializers
- [init(descriptor: PortalMaterial.Program.Descriptor) async throws](./program-swift.struct/init%28descriptor%29.md)
  Compiles a program from the given descriptor.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the shader program
- [var program: PortalMaterial.Program](./program-swift.property.md)
  The compiled program that drives this material’s surface and geometry shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct)*