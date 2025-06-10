# Package.Dependency.RegistryRequirement

**Framework**: PackageDescription  
**Kind**: enum

An enum that represents the requirement for a package dependency.

**Availability**:
- SwiftPM 999.0+

## Declaration

```swift
enum RegistryRequirement
```

#### Overview

Decide whether your project accepts updates to a package dependency up to the next major version or up to the next minor version. To be more restrictive, select a specific version range or an exact version. Major versions tend to have more significant changes than minor versions, and may require you to modify your code when they update. The version rule requires Swift packages to conform to semantic versioning. To learn more about the semantic versioning standard, visit the [`Semantic Versioning 2.0.0`](https://developer.apple.comhttps://semver.org) website.

## Topics

### Enumeration Cases
- [Package.Dependency.RegistryRequirement.exact(_:)](package/dependency/registryrequirement/exact(_:).md)
  A requirement based on an exact version.
- [Package.Dependency.RegistryRequirement.range(_:)](package/dependency/registryrequirement/range(_:).md)
  A requirement based on a range of versions.

## See Also

- [let traits: Set<Package.Dependency.Trait>](package/dependency/traits.md)
  The dependencies traits configuration.
- [Package.Dependency.Trait](package/dependency/trait.md)
  A struct representing an enabled trait of a dependency.
- [Package.Dependency.SourceControlRequirement](package/dependency/sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.
- [var requirement: Package.Dependency.Requirement](package/dependency/requirement-swift.property.md)
  The dependency requirement of the package dependency.
- [Package.Dependency.Requirement](package/dependency/requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/registryrequirement)*