# package(id:from:traits:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Adds a remote package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(id: String, from version: Version, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

This is the recommended way to specify a remote package dependency. It allows you to specify the minimum version you require, allows updates that include bug fixes and backward-compatible feature updates, but requires you to explicitly update to a new major version of the dependency. This approach provides the maximum flexibility on which version to use, while making sure you don’t update to a version with breaking changes, and helps to prevent conflicts in your dependency graph.

The following example allows the Swift Package Manager to select a version like a  `1.2.3`, `1.2.4`, or `1.3.0`, but not `2.0.0`.

```swift
.package(id: "scope.name", from: "1.2.3"),
```

## Parameters

- `id`: The identity of the package.
- `version`: The minimum version requirement.
- `traits`: The trait configuration of this dependency. The default value enables the default traits of the package.

## See Also

### Creating a package dependency from a registry
- [static func package(id: String, from: Version) -> Package.Dependency](./package%28id,from%29.md)
  Adds a remote package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, Range<Version>) -> Package.Dependency](./package%28id,_%29-27raa.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28id,_,traits%29-5rb8r.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, ClosedRange<Version>) -> Package.Dependency](./package%28id,_%29-6anr7.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28id,_,traits%29-5x94p.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, exact: Version) -> Package.Dependency](./package%28id,exact%29.md)
  Adds a remote package dependency with an exact version requirement.
- [static func package(id: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28id,exact,traits%29.md)
  Adds a remote package dependency with an exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(id:from:traits:))*