# package(url:from:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, from version: Version, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

This is the recommended way to specify a remote package dependency. It allows you to specify the minimum version you require, allows updates that include bug fixes and backward-compatible feature updates, but requires you to explicitly update to a new major version of the dependency. This approach provides the maximum flexibility on which version to use, while making sure you don’t update to a version with breaking changes, and helps to prevent conflicts in your dependency graph.

The following example allows the Swift Package Manager to select a version like a  `1.2.3`, `1.2.4`, or `1.3.0`, but not `2.0.0`.

```swift
.package(url: "https://example.com/example-package.git", from: "1.2.3"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `version`: The minimum version requirement.
- `traits`: The trait configuration of this dependency. The default value enables the default traits of the package.

## See Also

- [static func package(url: String, from: Version) -> Package.Dependency](package/dependency/package(url:from:).md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](package/dependency/package(url:_:)-2ys47.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-5pt81.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(url:_:)-1r6rc.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-mjzv.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, branch: String) -> Package.Dependency](package/dependency/package(url:branch:).md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(url: String, branch: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:branch:traits:).md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(url: String, revision: String) -> Package.Dependency](package/dependency/package(url:revision:).md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, revision: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:revision:traits:).md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, exact: Version) -> Package.Dependency](package/dependency/package(url:exact:).md)
  Adds a remote package dependency that uses an exact version requirement.
- [static func package(url: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:exact:traits:).md)
  Adds a remote package dependency that uses an exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:from:traits:))*