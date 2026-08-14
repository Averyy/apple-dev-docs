# Package.Dependency.Trait

**Framework**: PackageDescription  
**Kind**: struct

An enabled trait of a dependency.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Trait
```

## Topics

### Structures
- [Package.Dependency.Trait.Condition](package/dependency/trait/condition-swift.struct.md)
  A condition that limits the application of a trait for a dependency.
### Initializers
- [init(name: String, condition: Package.Dependency.Trait.Condition?)](package/dependency/trait/init(name:condition:).md)
  Creates a new enabled trait.
- [init(stringLiteral: StringLiteralType)](package/dependency/trait/init(stringliteral:).md)
  Creates a new enabled trait.
### Instance Properties
- [var condition: Package.Dependency.Trait.Condition?](package/dependency/trait/condition-swift.property.md)
  The condition under which the package manager enables the dependency.
- [var name: String](package/dependency/trait/name.md)
  The name of the enabled trait.
### Type Properties
- [static let defaults: Package.Dependency.Trait](package/dependency/trait/defaults.md)
  Enables all default traits of the dependency.
### Type Methods
- [static func trait(name: String, condition: Package.Dependency.Trait.Condition?) -> Package.Dependency.Trait](package/dependency/trait/trait(name:condition:).md)
  Creates a new enabled trait.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let traits: Set<Package.Dependency.Trait>](package/dependency/traits.md)
  The dependencies traits configuration.
- [Package.Dependency.RegistryRequirement](package/dependency/registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.SourceControlRequirement](package/dependency/sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.
- [var requirement: Package.Dependency.Requirement](package/dependency/requirement-swift.property.md)
  The dependency requirement of the package dependency.
- [Package.Dependency.Requirement](package/dependency/requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/trait)*