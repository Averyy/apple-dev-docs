# package(name:path:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Adds a local dependency to a named package located at the path you provide.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String, path: String) -> Package.Dependency
```

## Return Value

A package dependency.

## Discussion

If the package you depend on defines traits, the package manager uses the dependency with its default set of traits.

Swift Package Manager uses the package dependency as-is and doesn’t perform any source control access. Local package dependencies are especially useful during development of a new package or when working on multiple tightly coupled packages.

## Parameters

- `name`: The name of the Swift package.
- `path`: The file system path to the package.

## See Also

### Creating a local dependency
- [static func package(name: String, path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28name,path,traits%29.md)
  Adds a local dependency to a named package located at the path and with an optional set of traits you provide.
- [static func package(path: String) -> Package.Dependency](./package%28path%29.md)
  Adds a local dependency to a package located at the path you provide.
- [static func package(path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28path,traits%29.md)
  Adds a local dependency to a package located at the path and with an optional set of traits you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:path:))*