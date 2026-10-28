# Package.Dependency

**Framework**: PackageDescription  
**Kind**: class  
**Role**: Class

A package dependency of a Swift package.

## Declaration

```swift
class Dependency
```

## Overview

A package dependency consists of a Git URL to the source of the package, and a requirement for the version of the package.

Swift Package Manager performs a process called *dependency resolution* to determine the exact version of the package dependencies that an app or other Swift package can use. The `Package.resolved` file records the results of the dependency resolution and lives in the top-level directory of a Swift package. If you add the Swift package as a package dependency to an app for an Apple platform, you can find the `Package.resolved` file inside your `.xcodeproj` or `.xcworkspace`.

## Topics

### Creating a package dependency from a URL
- [static func package(url: String, from: Version) -> Package.Dependency](./dependency/package%28url,from%29.md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28url,from,traits%29.md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](./dependency/package%28url,_%29-2ys47.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28url,_,traits%29-5pt81.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](./dependency/package%28url,_%29-1r6rc.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28url,_,traits%29-mjzv.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, branch: String) -> Package.Dependency](./dependency/package%28url,branch%29.md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(url: String, branch: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28url,branch,traits%29.md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(url: String, revision: String) -> Package.Dependency](./dependency/package%28url,revision%29.md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, revision: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28url,revision,traits%29.md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, exact: Version) -> Package.Dependency](./dependency/package%28url,exact%29.md)
  Adds a remote package dependency that uses an exact version requirement.
- [static func package(url: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28url,exact,traits%29.md)
  Adds a remote package dependency that uses an exact version requirement.
### Creating a package dependency from a registry
- [static func package(id: String, from: Version) -> Package.Dependency](./dependency/package%28id,from%29.md)
  Adds a remote package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28id,from,traits%29.md)
  Adds a remote package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, Range<Version>) -> Package.Dependency](./dependency/package%28id,_%29-27raa.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28id,_,traits%29-5rb8r.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, ClosedRange<Version>) -> Package.Dependency](./dependency/package%28id,_%29-6anr7.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28id,_,traits%29-5x94p.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, exact: Version) -> Package.Dependency](./dependency/package%28id,exact%29.md)
  Adds a remote package dependency with an exact version requirement.
- [static func package(id: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28id,exact,traits%29.md)
  Adds a remote package dependency with an exact version requirement.
### Creating a local dependency
- [static func package(name: String, path: String) -> Package.Dependency](./dependency/package%28name,path%29.md)
  Adds a local dependency to a named package located at the path you provide.
- [static func package(name: String, path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28name,path,traits%29.md)
  Adds a local dependency to a named package located at the path and with an optional set of traits you provide.
- [static func package(path: String) -> Package.Dependency](./dependency/package%28path%29.md)
  Adds a local dependency to a package located at the path you provide.
- [static func package(path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./dependency/package%28path,traits%29.md)
  Adds a local dependency to a package located at the path and with an optional set of traits you provide.
### Declaring Requirements
- [let traits: Set<Package.Dependency.Trait>](./dependency/traits.md)
  The dependencies traits configuration.
- [Package.Dependency.Trait](./dependency/trait.md)
  An enabled trait of a dependency.
- [Package.Dependency.RegistryRequirement](./dependency/registryrequirement.md)
  An enum that represents the requirement for a package dependency.
- [Package.Dependency.SourceControlRequirement](./dependency/sourcecontrolrequirement.md)
  An enum that represents the requirement for a package dependency.
- [var requirement: Package.Dependency.Requirement](./dependency/requirement-swift.property.md)
  The dependency requirement of the package dependency.
- [Package.Dependency.Requirement](./dependency/requirement-swift.enum.md)
  An enum that represents the requirement for a package dependency.
### Describing a Package Dependency
- [let kind: Package.Dependency.Kind](./dependency/kind-swift.property.md)
  A description of the package dependency.
- [Package.Dependency.Kind](./dependency/kind-swift.enum.md)
  The type of dependency.
- [struct Version](../version.md)
  A version according to the semantic versioning specification.
- [var name: String?](./dependency/name.md)
  The name of the dependency.
- [var url: String?](./dependency/url.md)
  The Git URL of the package dependency.
### Deprecated methods
- [static func package(name: String?, url: String, Package.Dependency.Requirement) -> Package.Dependency](./dependency/package%28name,url,_%29-6k3na.md)
  Adds a remote package dependency with a given version requirement.
- [static func package(name: String, url: String, Range<Version>) -> Package.Dependency](./dependency/package%28name,url,_%29-nqbk.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(name: String, url: String, ClosedRange<Version>) -> Package.Dependency](./dependency/package%28name,url,_%29-7zltl.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(name: String, url: String, branch: String) -> Package.Dependency](./dependency/package%28name,url,branch%29.md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(name: String, url: String, from: Version) -> Package.Dependency](./dependency/package%28name,url,from%29.md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(name: String, url: String, revision: String) -> Package.Dependency](./dependency/package%28name,url,revision%29.md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, Package.Dependency.Requirement) -> Package.Dependency](./dependency/package%28url,_%29-4tkwi.md)
  Adds a remote package dependency given a version requirement.
- [var name: String?](./dependency/name.md)
  The name of the dependency.
- [var url: String?](./dependency/url.md)
  The Git URL of the package dependency.

## See Also

### Declaring Package Dependencies
- [var dependencies: [Package.Dependency]](./dependencies.md)
  The list of package dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency)*