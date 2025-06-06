# package(name:path:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a dependency to a package located at the given path on the filesystem.

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
- `traits`: The trait configuration of this dependency. Defaults to enabling the default traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:path:traits:))*