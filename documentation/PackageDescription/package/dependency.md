# Package.Dependency

**Framework**: PackageDescription  
**Kind**: class

A package dependency of a Swift package.

## Declaration

```swift
class Dependency
```

#### Overview

A package dependency consists of a Git URL to the source of the package, and a requirement for the version of the package.

Swift Package Manager performs a process called  to determine the exact version of the package dependencies that an app or other Swift package can use. The `Package.resolved` file records the results of the dependency resolution and lives in the top-level directory of a Swift package. If you add the Swift package as a package dependency to an app for an Apple platform, you can find the `Package.resolved` file inside your `.xcodeproj` or `.xcworkspace`.

## Topics

### Creating a Package Dependency
- [static func package(name: String, path: String) -> Package.Dependency](package/dependency/package(name:path:).md)
  Adds a dependency to a package located at the given path on the filesystem.
- [static func package(url: String, from: Version) -> Package.Dependency](package/dependency/package(url:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](package/dependency/package(url:_:)-2ys47.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(url:_:)-1r6rc.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, branch: String) -> Package.Dependency](package/dependency/package(url:branch:).md)
  Adds a remote package dependency given a branch requirement.
- [static func package(url: String, revision: String) -> Package.Dependency](package/dependency/package(url:revision:).md)
  Adds a remote package dependency given a revision requirement.
- [static func package(url: String, exact: Version) -> Package.Dependency](package/dependency/package(url:exact:).md)
  Adds a package dependency that uses the exact version requirement.
- [static func package(path: String) -> Package.Dependency](package/dependency/package(path:).md)
  Adds a dependency to a package located at the given path.
### Declaring Requirements
- [var requirement: Package.Dependency.Requirement](package/dependency/requirement-swift.property.md)
  The dependency requirement of the package dependency.
- [Package.Dependency.Requirement](package/dependency/requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.
### Describing a Package Dependency
- [let kind: Package.Dependency.Kind](package/dependency/kind-swift.property.md)
  A description of the package dependency.
- [struct Version](version.md)
  A version according to the semantic versioning specification.
### Structures
- [Package.Dependency.Trait](package/dependency/trait.md)
  A struct representing an enabled trait of a dependency.
### Instance Properties
- [var name: String?](package/dependency/name.md)
  The name of the dependency.
- [let traits: Set<Package.Dependency.Trait>](package/dependency/traits.md)
  The dependencies traits configuration.
- [var url: String?](package/dependency/url.md)
  The Git URL of the package dependency.
### Type Methods
- [static func package(id: String, Range<Version>) -> Package.Dependency](package/dependency/package(id:_:)-27raa.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(id:_:)-6anr7.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:_:traits:)-5rb8r.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:_:traits:)-5x94p.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, exact: Version) -> Package.Dependency](package/dependency/package(id:exact:).md)
  Adds a package dependency that uses the exact version requirement.
- [static func package(id: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:exact:traits:).md)
  Adds a package dependency that uses the exact version requirement.
- [static func package(id: String, from: Version) -> Package.Dependency](package/dependency/package(id:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:from:traits:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(name: String, path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(name:path:traits:).md)
  Adds a dependency to a package located at the given path on the filesystem.
- [static func package(name: String?, url: String, Package.Dependency.Requirement) -> Package.Dependency](package/dependency/package(name:url:_:)-6k3na.md)
  Adds a remote package dependency with a given version requirement.
- [static func package(name: String, url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(name:url:_:)-7zltl.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(name: String, url: String, Range<Version>) -> Package.Dependency](package/dependency/package(name:url:_:)-nqbk.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(name: String, url: String, branch: String) -> Package.Dependency](package/dependency/package(name:url:branch:).md)
  Adds a remote package dependency given a branch requirement.
- [static func package(name: String, url: String, from: Version) -> Package.Dependency](package/dependency/package(name:url:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(name: String, url: String, revision: String) -> Package.Dependency](package/dependency/package(name:url:revision:).md)
  Adds a remote package dependency given a revision requirement.
- [static func package(path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(path:traits:).md)
  Adds a dependency to a package located at the given path.
- [static func package(url: String, Package.Dependency.Requirement) -> Package.Dependency](package/dependency/package(url:_:)-4tkwi.md)
  Adds a remote package dependency given a version requirement.
- [static func package(url: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-5pt81.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-mjzv.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, branch: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:branch:traits:).md)
  Adds a remote package dependency given a branch requirement.
- [static func package(url: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:exact:traits:).md)
  Adds a package dependency that uses the exact version requirement.
- [static func package(url: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:from:traits:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, revision: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:revision:traits:).md)
  Adds a remote package dependency given a revision requirement.
### Enumerations
- [Package.Dependency.Kind](package/dependency/kind-swift.enum.md)
  The type of dependency.
- [Package.Dependency.RegistryRequirement](package/dependency/registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.SourceControlRequirement](package/dependency/sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.

## See Also

- [var dependencies: [Package.Dependency]](package/dependencies.md)
  The list of package dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency)*