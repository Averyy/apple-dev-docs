# package(path:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a dependency to a package located at the given path.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(path: String, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A package dependency.

#### Discussion

The Swift Package Manager uses the package dependency as-is and does not perform any source control access. Local package dependencies are especially useful during development of a new package or when working on multiple tightly coupled packages.

## Parameters

- `path`: The file system path to the package.
- `traits`: The trait configuration of this dependency. Defaults to enabling the default traits.

## See Also

- [static func package(name: String, path: String) -> Package.Dependency](package/dependency/package(name:path:).md)
  Adds a dependency to a package located at the given path on the filesystem.
- [static func package(name: String, path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(name:path:traits:).md)
  Adds a dependency to a package located at the given path on the filesystem.
- [static func package(path: String) -> Package.Dependency](package/dependency/package(path:).md)
  Adds a dependency to a package located at the given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(path:traits:))*