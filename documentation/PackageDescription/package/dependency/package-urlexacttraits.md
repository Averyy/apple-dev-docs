# package(url:exact:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency that uses the exact version requirement.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, exact version: Version, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

Specifying exact version requirements are not recommended as they can cause conflicts in your dependency graph when other packages depend on this package. As Swift packages follow the semantic versioning convention, think about specifying a version range instead.

The following example instructs the Swift Package Manager to use version `1.2.3`.

```swift
.package(url: "https://example.com/example-package.git", exact: "1.2.3"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `version`: The exact version of the dependency for this requirement.
- `traits`: The trait configuration of this dependency.  Defaults to enabling the default traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:exact:traits:))*