# package(url:_:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, _ range: ClosedRange<Version>, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions 1.2.3, 1.2.4, 1.2.5, as well as 1.2.6.

```swift
.package(url: "https://example.com/example-package.git", "1.2.3"..."1.2.6"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `range`: The closed version range requirement.
- `traits`: The trait configuration of this dependency. The default value enables the default traits of the package.

## See Also

- [static func package(url: String, from: Version) -> Package.Dependency](package/dependency/package(url:from:).md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:from:traits:).md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](package/dependency/package(url:_:)-2ys47.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-5pt81.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(url:_:)-1r6rc.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:_:traits:)-mjzv)*