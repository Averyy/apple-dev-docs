# PortalMaterial.Program

**Framework**: RealityKit  
**Kind**: struct

A compiled shader program that drives the appearance of a portal’s surface and geometry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Program
```

## Topics

### Configuring the program
- [var descriptor: PortalMaterial.Program.Descriptor](portalmaterial/program-swift.struct/descriptor-swift.property.md)
  The descriptor that produced this program.
- [PortalMaterial.Program.Descriptor](portalmaterial/program-swift.struct/descriptor-swift.struct.md)
  Configuration used to compile a [`PortalMaterial.Program`](portalmaterial/program-swift.struct.md).
### Initializers
- [init(descriptor: PortalMaterial.Program.Descriptor) async throws](portalmaterial/program-swift.struct/init(descriptor:).md)
  Compiles a program from the given descriptor.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var program: PortalMaterial.Program](portalmaterial/program-swift.property.md)
  The compiled program that drives this material’s surface and geometry shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct)*