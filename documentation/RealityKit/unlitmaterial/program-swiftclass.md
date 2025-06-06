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
- [UnlitMaterial.Program.Descriptor](unlitmaterial/program-swift.class/descriptor-swift.struct.md)
  An object that specifies all parameters necessary to initialize `UnlitMaterial` programs
### Operators
- [static func == (UnlitMaterial.Program, UnlitMaterial.Program) -> Bool](unlitmaterial/program-swift.class/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(descriptor: UnlitMaterial.Program.Descriptor) async](unlitmaterial/program-swift.class/init(descriptor:).md)
### Instance Properties
- [let descriptor: UnlitMaterial.Program.Descriptor](unlitmaterial/program-swift.class/descriptor-swift.property.md)
- [var hashValue: Int](unlitmaterial/program-swift.class/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](unlitmaterial/program-swift.class/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](unlitmaterial/program-swift.class/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/program-swift.class)*