# package(name:url:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency with a given version requirement.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String?, url: String, _ requirement: Package.Dependency.Requirement) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

## Parameters

- `name`: The name of the Swift package or   to deduce the name from the package’s Git URL.
- `url`: The valid Git URL of the package.
- `requirement`: A dependency requirement. See static methods on    for available options.

## See Also

- [static func package(name: String, url: String, Range<Version>) -> Package.Dependency](package/dependency/package(name:url:_:)-nqbk.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:_:)-6k3na)*