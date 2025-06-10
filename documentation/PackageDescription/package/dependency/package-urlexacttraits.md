# package(url:exact:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency that uses the exact version requirement.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, exact version: Version, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

Specifying exact version requirements are not recommended as they can cause conflicts in your dependency graph when other packages depend on this package. As Swift packages follow the semantic versioning convention, think about specifying a version range instead.

The following example instructs the Swift Package Manager to use version `1.2.3`.

```swift
.package(url: "https://example.com/example-package.git", exact: "1.2.3"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `version`: The exact version of the dependency for this requirement.
- `traits`: The trait configuration of this dependency.  Defaults to enabling the default traits.

## See Also

- [static func package(url: String, from: Version) -> Package.Dependency](package/dependency/package(url:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:from:traits:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](package/dependency/package(url:_:)-2ys47.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-5pt81.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(url:_:)-1r6rc.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:_:traits:)-mjzv.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, branch: String) -> Package.Dependency](package/dependency/package(url:branch:).md)
  Adds a remote package dependency given a branch requirement.
- [static func package(url: String, branch: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:branch:traits:).md)
  Adds a remote package dependency given a branch requirement.
- [static func package(url: String, revision: String) -> Package.Dependency](package/dependency/package(url:revision:).md)
  Adds a remote package dependency given a revision requirement.
- [static func package(url: String, revision: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:revision:traits:).md)
  Adds a remote package dependency given a revision requirement.
- [static func package(url: String, exact: Version) -> Package.Dependency](package/dependency/package(url:exact:).md)
  Adds a package dependency that uses the exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:exact:traits:))*