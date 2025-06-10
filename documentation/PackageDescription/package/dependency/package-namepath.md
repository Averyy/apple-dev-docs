# package(name:path:)

**Framework**: PackageDescription  
**Kind**: method

Adds a dependency to a package located at the given path on the filesystem.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String, path: String) -> Package.Dependency
```

#### Return Value

A package dependency.

#### Discussion

Swift Package Manager uses the package dependency as-is and doesn’t perform any source control access. Local package dependencies are especially useful during development of a new package or when working on multiple tightly coupled packages.

## Parameters

- `name`: The name of the Swift package.
- `path`: The file system path to the package.

## See Also

- [static func package(name: String, path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(name:path:traits:).md)
  Adds a dependency to a package located at the given path on the filesystem.
- [static func package(path: String) -> Package.Dependency](package/dependency/package(path:).md)
  Adds a dependency to a package located at the given path.
- [static func package(path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(path:traits:).md)
  Adds a dependency to a package located at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:path:))*