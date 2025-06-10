# Target.TargetType

**Framework**: PackageDescription  
**Kind**: enum

The different types of a target.

## Declaration

```swift
enum TargetType
```

## Topics

### Enumeration Cases
- [Target.TargetType.regular](target/targettype/regular.md)
  A target that contains code for the Swift package’s functionality.
- [Target.TargetType.binary](target/targettype/binary.md)
  A target that references a binary artifact.
- [Target.TargetType.system](target/targettype/system.md)
  A target that adapts a library on the system to work with Swift packages.
- [Target.TargetType.test](target/targettype/test.md)
  A target that contains tests for the Swift package’s other targets.
- [Target.TargetType.executable](target/targettype/executable.md)
  A target that contains code for an executable’s main module.
- [Target.TargetType.plugin](target/targettype/plugin.md)
  A target that provides a package plug-in.
- [Target.TargetType.macro](target/targettype/macro.md)
  A target that provides a Swift macro.
### Creating a Value
- [init?(rawValue: String)](target/targettype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Hashing
- [func hash(into: inout Hasher)](target/targettype/hash(into:).md)
  Hashes the target type by feeding the item into the given hasher.
- [var hashValue: Int](target/targettype/hashvalue.md)
  The target type’s hash value.
### Operator Functions
- [static func != (Self, Self) -> Bool](target/targettype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Instance Properties
- [var rawValue: String](target/targettype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Target.TargetType.RawValue](target/targettype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](target/targettype/equatable-implementations.md)
- [RawRepresentable Implementations](target/targettype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var isTest: Bool](target/istest.md)
  A Boolean value that indicates whether this is a test target.
- [let type: Target.TargetType](target/type.md)
  The type of the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/targettype)*