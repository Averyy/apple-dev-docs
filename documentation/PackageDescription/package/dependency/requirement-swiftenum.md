# Package.Dependency.Requirement

**Framework**: PackageDescription  
**Kind**: enum

An enum that represents the requirement for a package dependency.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
enum Requirement
```

#### Overview

The dependency requirement can be defined as one of three different version requirements:

The version rule requires Swift packages to conform to semantic versioning. To learn more about the semantic versioning standard, visit the [`Semantic Versioning 2.0.0`](https://developer.apple.comhttps://semver.org) website.

Selecting the version requirement is the recommended way to add a package dependency. It allows you to create a balance between restricting changes and obtaining improvements and features. - term A branch-based requirement: Select the name of the branch for your package dependency to follow. Use branch-based dependencies when you’re developing multiple packages in tandem or when you don’t want to publish versions of your package dependencies.

Note that packages which use branch-based dependency requirements can’t be added as dependencies to packages that use version-based dependency requirements; you should remove branch-based dependency requirements before publishing a version of your package. - term A commit-based requirement: Select the commit hash for your package dependency to follow.

Choosing this option isn’t recommended, and should be limited to exceptional cases. While pinning your package dependency to a specific commit ensures that the package dependency doesn’t change and your code remains stable, you don’t receive any updates at all. If you worry about the stability of a remote package, consider one of the more restrictive options of the version-based requirement.

Note that packages which use commit-based dependency requirements can’t be added as dependencies to packages that use version-based dependency requirements; you should remove commit-based dependency requirements before publishing a version of your package.

## Topics

### Enumeration Cases
- [Package.Dependency.Requirement.branchItem(_:)](package/dependency/requirement-swift.enum/branchitem(_:).md)
- [Package.Dependency.Requirement.exactItem(_:)](package/dependency/requirement-swift.enum/exactitem(_:).md)
- [Package.Dependency.Requirement.localPackageItem](package/dependency/requirement-swift.enum/localpackageitem.md)
- [Package.Dependency.Requirement.rangeItem(_:)](package/dependency/requirement-swift.enum/rangeitem(_:).md)
- [Package.Dependency.Requirement.revisionItem(_:)](package/dependency/requirement-swift.enum/revisionitem(_:).md)
### Type Methods
- [static func branch(String) -> Package.Dependency.Requirement](package/dependency/requirement-swift.enum/branch(_:).md)
  Returns a requirement for a source control branch.
- [static func exact(Version) -> Package.Dependency.Requirement](package/dependency/requirement-swift.enum/exact(_:).md)
  Returns a requirement for the given exact version.
- [static func revision(String) -> Package.Dependency.Requirement](package/dependency/requirement-swift.enum/revision(_:).md)
  Returns a requirement for a source control revision such as the hash of a commit.
- [static func upToNextMajor(from: Version) -> Package.Dependency.Requirement](package/dependency/requirement-swift.enum/uptonextmajor(from:).md)
  A source control requirement bounded to the given version’s major version number.
- [static func upToNextMinor(from: Version) -> Package.Dependency.Requirement](package/dependency/requirement-swift.enum/uptonextminor(from:).md)
  A source control requirement bounded to the given version’s minor version number.

## See Also

- [let traits: Set<Package.Dependency.Trait>](package/dependency/traits.md)
  The dependencies traits configuration.
- [Package.Dependency.Trait](package/dependency/trait.md)
  A struct representing an enabled trait of a dependency.
- [Package.Dependency.RegistryRequirement](package/dependency/registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.SourceControlRequirement](package/dependency/sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.
- [var requirement: Package.Dependency.Requirement](package/dependency/requirement-swift.property.md)
  The dependency requirement of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/requirement-swift.enum)*