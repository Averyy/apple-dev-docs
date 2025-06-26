# UnlitMaterial.Program

**Framework**: RealityKit  
**Kind**: class

An object that represents the backing shader compilation required for unlit materials.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
final class Program
```

#### Overview

You can use this type to control when RealityKit compiles shaders, and to initialize `UnlitMaterial` objects with more predicitable loading performance.

When initializing an `UnlitMaterial` this way, a `Program` object is created first asynchronously, which is used to cache the material’s shader program so the `UnlitMaterial` can be loaded immediately later.

For example:

```swift
// Initialize descriptor with desired properties
var descriptor = UnlitMaterial.Descriptor()
descriptor.applyPostProcessToneMap = false

// Create program object
let program = await UnlitMaterial.Program(descriptor: descriptor)

// Create material (returns immediately)
let material = UnlitMaterial(program: program)
```

## Topics

### Structures
- [UnlitMaterial.Program.Descriptor](unlitmaterial/program-7swyg/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `UnlitMaterial` programs
### Initializers
- [init(descriptor:)](unlitmaterial/program-9tv7i/init(descriptor:).md)
### Instance Properties
- [let descriptor: UnlitMaterial.Program.Descriptor](unlitmaterial/program-7swyg/descriptor-swift.property.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/program-7swyg)*