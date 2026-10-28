# package(name:url:branch:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Adds a remote package dependency with a branch requirement you provide.

**Availability**:
- SwiftPM 5.5+ - Deprecated in 5.6

> **Deprecated**: use package(url:branch:) instead

## Declaration

```swift
static func package(name: String, url: String, branch: String) -> Package.Dependency
```

## Return Value

A `Package.Dependency` instance.

## Discussion

```swift
.package(url: "https://example.com/example-package.git", branch: "main"),
```

## Parameters

- `name`: The name of the package, or nil to deduce it from the URL.
- `url`: The valid Git URL of the package.
- `branch`: A dependency requirement. See static methods on [`Package.Dependency.Requirement`](./requirement-swift.enum.md) for available options.

## See Also

### Deprecated methods
- [static func package(name: String?, url: String, Package.Dependency.Requirement) -> Package.Dependency](./package%28name,url,_%29-6k3na.md)
  Adds a remote package dependency with a given version requirement.
- [static func package(name: String, url: String, Range<Version>) -> Package.Dependency](./package%28name,url,_%29-nqbk.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(name: String, url: String, ClosedRange<Version>) -> Package.Dependency](./package%28name,url,_%29-7zltl.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(name: String, url: String, from: Version) -> Package.Dependency](./package%28name,url,from%29.md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(name: String, url: String, revision: String) -> Package.Dependency](./package%28name,url,revision%29.md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, Package.Dependency.Requirement) -> Package.Dependency](./package%28url,_%29-4tkwi.md)
  Adds a remote package dependency given a version requirement.
- [var name: String?](./name.md)
  The name of the dependency.
- [var url: String?](./url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:branch:))*