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

#### Overview

Marked `@unchecked Sendable` because it stores a class reference (`__MaterialResource`). This is safe as long as the reference is never reassigned after `init`, and the underlying CoreRE asset uses thread-safe reference counting, so sharing a `Program` across threads is fine.

## Topics

### Configuring the program
- [var descriptor: PortalMaterial.Program.Descriptor](portalmaterial/program-swift.struct/descriptor-swift.property.md)
  The descriptor used to create this program.
- [PortalMaterial.Program.Descriptor](portalmaterial/program-swift.struct/descriptor-swift.struct.md)
  Configuration used to compile a [`PortalMaterial.Program`](portalmaterial/program-swift.struct.md).
### Initializers
- [init(descriptor: PortalMaterial.Program.Descriptor) async throws](portalmaterial/program-swift.struct/init(descriptor:).md)
  Creates a program by compiling the shader node graph in the given descriptor.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var program: PortalMaterial.Program](portalmaterial/program-swift.property.md)
  The compiled program that defines this material’s shading behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalmaterial/program-swift.struct)*