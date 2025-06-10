# Package.Dependency.SourceControlRequirement

**Framework**: PackageDescription  
**Kind**: enum

An enum that represents the requirement for a package dependency.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
enum SourceControlRequirement
```

#### Overview

The dependency requirement can be defined as one of three different version requirements:

Decide whether your project accepts updates to a package dependency up to the next major version or up to the next minor version. To be more restrictive, select a specific version range or an exact version. Major versions tend to have more significant changes than minor versions, and may require you to modify your code when they update. The version rule requires Swift packages to conform to semantic versioning. To learn more about the semantic versioning standard, see the [`Semantic Versioning 2.0.0`](https://developer.apple.comhttps://semver.org) website.

Selecting the version requirement is the recommended way to add a package dependency. It allows you to create a balance between restricting changes and obtaining improvements and features.

Select the name of the branch for your package dependency to follow. Use branch-based dependencies when you’re developing multiple packages in tandem or when you don’t want to publish versions of your package dependencies.

Note that packages which use branch-based dependency requirements can’t be added as dependencies to packages that use version-based dependency requirements; you should remove branch-based dependency requirements before publishing a version of your package.

Select the commit hash for your package dependency to follow. Choosing this option isn’t recommended, and should be limited to exceptional cases. While pinning your package dependency to a specific commit ensures that the package dependency doesn’t change and your code remains stable, you don’t receive any updates at all. If you worry about the stability of a remote package, consider one of the more restrictive options of the version-based requirement.

Note that packages which use commit-based dependency requirements can’t be added as dependencies to packages that use version-based dependency requirements; you should remove commit-based dependency requirements before publishing a version of your package.

## Topics

### Enumeration Cases
- [Package.Dependency.SourceControlRequirement.branch(_:)](package/dependency/sourcecontrolrequirement/branch(_:).md)
  A branch based requirement.
- [Package.Dependency.SourceControlRequirement.exact(_:)](package/dependency/sourcecontrolrequirement/exact(_:).md)
  An exact version based requirement.
- [Package.Dependency.SourceControlRequirement.range(_:)](package/dependency/sourcecontrolrequirement/range(_:).md)
  A requirement based on a range of versions.
- [Package.Dependency.SourceControlRequirement.revision(_:)](package/dependency/sourcecontrolrequirement/revision(_:).md)
  A commit based requirement.

## See Also

- [let traits: Set<Package.Dependency.Trait>](package/dependency/traits.md)
  The dependencies traits configuration.
- [Package.Dependency.Trait](package/dependency/trait.md)
  A struct representing an enabled trait of a dependency.
- [Package.Dependency.RegistryRequirement](package/dependency/registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [var requirement: Package.Dependency.Requirement](package/dependency/requirement-swift.property.md)
  The dependency requirement of the package dependency.
- [Package.Dependency.Requirement](package/dependency/requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/sourcecontrolrequirement)*