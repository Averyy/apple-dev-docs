# Package.Dependency.Trait

**Framework**: PackageDescription  
**Kind**: struct  
**Role**: Structure

An enabled trait of a dependency.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Trait
```

## Topics

### Structures
- [Package.Dependency.Trait.Condition](./trait/condition-swift.struct.md)
  A condition that limits the application of a trait for a dependency.
### Initializers
- [init(name: String, condition: Package.Dependency.Trait.Condition?)](./trait/init%28name,condition%29.md)
  Creates a new enabled trait.
- [init(stringLiteral: StringLiteralType)](./trait/init%28stringliteral%29.md)
  Creates a new enabled trait.
### Instance Properties
- [var condition: Package.Dependency.Trait.Condition?](./trait/condition-swift.property.md)
  The condition under which the package manager enables the dependency.
- [var name: String](./trait/name.md)
  The name of the enabled trait.
### Type Properties
- [static let defaults: Package.Dependency.Trait](./trait/defaults.md)
  Enables all default traits of the dependency.
### Type Methods
- [static func trait(name: String, condition: Package.Dependency.Trait.Condition?) -> Package.Dependency.Trait](./trait/trait%28name,condition%29.md)
  Creates a new enabled trait.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Declaring Requirements
- [let traits: Set<Package.Dependency.Trait>](./traits.md)
  The dependencies traits configuration.
- [Package.Dependency.RegistryRequirement](./registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.SourceControlRequirement](./sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.
- [var requirement: Package.Dependency.Requirement](./requirement-swift.property.md)
  The dependency requirement of the package dependency.
- [Package.Dependency.Requirement](./requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/trait)*