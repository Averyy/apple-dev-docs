# package(path:)

**Framework**: PackageDescription  
**Kind**: method

Adds a local dependency to a package located at the path you provide.

## Declaration

```swift
static func package(path: String) -> Package.Dependency
```

#### Return Value

A package dependency.

#### Discussion

If the package you depend on defines traits, the package manager uses the dependency with its default set of traits.

The Swift Package Manager uses the package dependency as-is and does not perform any source control access. Local package dependencies are especially useful during development of a new package or when working on multiple tightly coupled packages.

## Parameters

- `path`: The file system path to the package.

## See Also

- [static func package(name: String, path: String) -> Package.Dependency](package/dependency/package(name:path:).md)
  Adds a local dependency to a named package located at the path you provide.
- [static func package(name: String, path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(name:path:traits:).md)
  Adds a local dependency to a named package located at the path and with an optional set of traits you provide.
- [static func package(path: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(path:traits:).md)
  Adds a local dependency to a package located at the path and with an optional set of traits you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(path:))*