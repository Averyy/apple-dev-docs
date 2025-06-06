# PhysicallyBasedMaterial.Program

**Framework**: RealityKit  
**Kind**: class

An object that represents the backing shader compilation required for physically based materials.

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

You can use this type to control when RealityKit compiles shaders, and to initialize `PhysicallyBasedMaterial` objects with more predicitable loading performance.

When initializing a `PhysicallyBasedMaterial` this way, a `Program` object is created first asynchronously, which is used to cache the material’s shader program so the `PhysicallyBasedMaterial` can be loaded immediately later.

For example:

```swift
// Initialize descriptor with desired properties
var descriptor = PhysicallyBasedMaterial.Descriptor()
descriptor.blendMode = .add

// Create program object
let program = await PhysicallyBasedMaterial.Program(descriptor: descriptor)

// Create material (returns immediately)
let material = PhysicallyBasedMaterial(program: program)
```

## Topics

### Structures
- [PhysicallyBasedMaterial.Program.Descriptor](physicallybasedmaterial/program-swift.class/descriptor-swift.struct.md)
  Specifies all parameters necessary to initialize `PhysicallyBasedMaterial` programs
### Operators
- [static func == (PhysicallyBasedMaterial.Program, PhysicallyBasedMaterial.Program) -> Bool](physicallybasedmaterial/program-swift.class/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(descriptor: PhysicallyBasedMaterial.Program.Descriptor) async](physicallybasedmaterial/program-swift.class/init(descriptor:).md)
### Instance Properties
- [let descriptor: PhysicallyBasedMaterial.Program.Descriptor](physicallybasedmaterial/program-swift.class/descriptor-swift.property.md)
- [var hashValue: Int](physicallybasedmaterial/program-swift.class/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](physicallybasedmaterial/program-swift.class/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](physicallybasedmaterial/program-swift.class/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/program-swift.class)*