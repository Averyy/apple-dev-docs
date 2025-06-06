# package(url:branch:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency given a branch requirement.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func package(url: String, branch: String) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

```swift
.package(url: "https://example.com/example-package.git", branch: "main"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `branch`: A dependency requirement. See static methods on   for available options.

## See Also

- [static func package(name: String, path: String) -> Package.Dependency](package/dependency/package(name:path:).md)
  Adds a dependency to a package located at the given path on the filesystem.
- [static func package(url: String, from: Version) -> Package.Dependency](package/dependency/package(url:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](package/dependency/package(url:_:)-2ys47.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(url:_:)-1r6rc.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, revision: String) -> Package.Dependency](package/dependency/package(url:revision:).md)
  Adds a remote package dependency given a revision requirement.
- [static func package(url: String, exact: Version) -> Package.Dependency](package/dependency/package(url:exact:).md)
  Adds a package dependency that uses the exact version requirement.
- [static func package(path: String) -> Package.Dependency](package/dependency/package(path:).md)
  Adds a dependency to a package located at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:branch:))*