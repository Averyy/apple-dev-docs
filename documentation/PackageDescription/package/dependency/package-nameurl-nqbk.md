# package(name:url:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String, url: String, _ range: Range<Version>) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions `1.2.3`, `1.2.4`, `1.2.5`, but not `1.2.6`.

```swift
.package(url: "https://example.com/example-package.git", "1.2.3"..<"1.2.6"),
```

## Parameters

- `name`: The name of the package, or   to deduce it from the URL.
- `url`: The valid Git URL of the package.
- `range`: The custom version range requirement.

## See Also

- [static func package(name: String?, url: String, Package.Dependency.Requirement) -> Package.Dependency](package/dependency/package(name:url:_:)-6k3na.md)
  Adds a remote package dependency with a given version requirement.
- [static func package(name: String, url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(name:url:_:)-7zltl.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(name: String, url: String, branch: String) -> Package.Dependency](package/dependency/package(name:url:branch:).md)
  Adds a remote package dependency given a branch requirement.
- [static func package(name: String, url: String, from: Version) -> Package.Dependency](package/dependency/package(name:url:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(name: String, url: String, revision: String) -> Package.Dependency](package/dependency/package(name:url:revision:).md)
  Adds a remote package dependency given a revision requirement.
- [static func package(url: String, Package.Dependency.Requirement) -> Package.Dependency](package/dependency/package(url:_:)-4tkwi.md)
  Adds a remote package dependency given a version requirement.
- [var name: String?](package/dependency/name.md)
  The name of the dependency.
- [var url: String?](package/dependency/url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:_:)-nqbk)*