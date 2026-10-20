# Target.TargetType

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

The different types of a target.

## Declaration

```swift
enum TargetType
```

## Topics

### Enumeration Cases
- [Target.TargetType.regular](./targettype/regular.md)
  A target that contains code for the Swift package’s functionality.
- [Target.TargetType.binary](./targettype/binary.md)
  A target that references a binary artifact.
- [Target.TargetType.system](./targettype/system.md)
  A target that adapts a library on the system to work with Swift packages.
- [Target.TargetType.test](./targettype/test.md)
  A target that contains tests for the Swift package’s other targets.
- [Target.TargetType.executable](./targettype/executable.md)
  A target that contains code for an executable’s main module.
- [Target.TargetType.plugin](./targettype/plugin.md)
  A target that provides a package plug-in.
- [Target.TargetType.macro](./targettype/macro.md)
  A target that provides a Swift macro.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Describing the Target Type
- [var isTest: Bool](./istest.md)
  A Boolean value that indicates whether this is a test target.
- [let type: Target.TargetType](./type.md)
  The type of the target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/targettype)*