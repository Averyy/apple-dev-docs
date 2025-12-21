# Package.Dependency.Trait

**Framework**: PackageDescription  
**Kind**: struct

A struct representing an enabled trait of a dependency.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Trait
```

## Topics

### Structures
- [Package.Dependency.Trait.Condition](package/dependency/trait/condition-swift.struct.md)
  A condition that limits the application of a dependencies trait.
### Initializers
- [init(name: String, condition: Package.Dependency.Trait.Condition?)](package/dependency/trait/init(name:condition:).md)
  Initializes a new enabled trait.
### Instance Properties
- [var condition: Package.Dependency.Trait.Condition?](package/dependency/trait/condition-swift.property.md)
  The condition under which the trait is enabled.
- [var name: String](package/dependency/trait/name.md)
  The name of the enabled trait.
### Type Properties
- [static let defaults: Package.Dependency.Trait](package/dependency/trait/defaults.md)
  Enables all default traits of a package.
### Type Methods
- [static func trait(name: String, condition: Package.Dependency.Trait.Condition?) -> Package.Dependency.Trait](package/dependency/trait/trait(name:condition:).md)
  Initializes a new enabled trait.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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