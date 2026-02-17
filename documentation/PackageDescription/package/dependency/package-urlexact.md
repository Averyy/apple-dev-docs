# package(url:exact:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency that uses an exact version requirement.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
static func package(url: String, exact version: Version) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

Specifying exact version requirements are not recommended as they can cause conflicts in your dependency graph when other packages depend on this package. As Swift packages follow the semantic versioning convention, think about specifying a version range instead.

The following example instructs the Swift Package Manager to use version `1.2.3`.

```swift
.package(url: "https://example.com/example-package.git", exact: "1.2.3"),
```

If the package you depend on defines traits, the package manager uses the dependency with its default set of traits.

## Parameters

- `url`: The valid Git URL of the package.
- `version`: The exact version of the dependency for this requirement.

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
- [static func package(url: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(url:exact:traits:).md)
  Adds a remote package dependency that uses an exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:exact:))*