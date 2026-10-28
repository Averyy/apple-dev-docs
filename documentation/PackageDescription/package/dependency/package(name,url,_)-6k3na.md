# package(name:url:_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Adds a remote package dependency with a given version requirement.

**Availability**:
- SwiftPM 5.2+ - Deprecated in 5.6

> **Deprecated**: use specific requirement APIs instead (e.g. use 'branch:' instead of '.branch')

## Declaration

```swift
static func package(name: String?, url: String, _ requirement: Package.Dependency.Requirement) -> Package.Dependency
```

## Return Value

A `Package.Dependency` instance.

## Parameters

- `name`: The name of the Swift package or `nil` to deduce the name from the package’s Git URL.
- `url`: The valid Git URL of the package.
- `requirement`: A dependency requirement. See static methods on [`Package.Dependency.Requirement`](./requirement-swift.enum.md) for available options.

## See Also

### Deprecated methods
- [static func package(name: String, url: String, Range<Version>) -> Package.Dependency](./package%28name,url,_%29-nqbk.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(name: String, url: String, ClosedRange<Version>) -> Package.Dependency](./package%28name,url,_%29-7zltl.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(name: String, url: String, branch: String) -> Package.Dependency](./package%28name,url,branch%29.md)
  Adds a remote package dependency with a branch requirement you provide.
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

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:_:)-6k3na)*