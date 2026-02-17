# package(name:path:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a local dependency to a named package located at the path and with an optional set of traits you provide.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(name: String, path: String, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A package dependency.

#### Discussion

Swift Package Manager uses the package dependency as-is and doesn’t perform any source control access. Local package dependencies are especially useful during development of a new package or when working on multiple tightly coupled packages.

## Parameters

- `name`: The name of the Swift package.
- `path`: The file system path to the package.
- `traits`: The trait configuration of this dependency. The default value enables the default traits of the package.

## See Also

- [static func package(name: String, path: String) -> Package.Dependency](package/dependency/package(name:path:).md)
  Adds a local dependency to a named package located at the path you provide.
- [static func package(path: String) -> Package.Dependency](package/dependency/package(path:).md)
  Adds a local dependency to a package located at the path you provide.
- [static func package(path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(path:traits:).md)
  Adds a local dependency to a package located at the path and with an optional set of traits you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:path:traits:))*