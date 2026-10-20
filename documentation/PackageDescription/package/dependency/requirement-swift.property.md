# requirement

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The dependency requirement of the package dependency.

**Availability**:
- SwiftPM - Deprecated in 5.6

> **Deprecated**: use kind instead

## Declaration

```swift
var requirement: Package.Dependency.Requirement { get }
```

## See Also

### Declaring Requirements
- [let traits: Set<Package.Dependency.Trait>](./traits.md)
  The dependencies traits configuration.
- [Package.Dependency.Trait](./trait.md)
  An enabled trait of a dependency.
- [Package.Dependency.RegistryRequirement](./registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.SourceControlRequirement](./sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.Requirement](./requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/requirement-swift.property)*