# package(url:revision:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency given a revision requirement.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, revision: String, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

```swift
.package(url: "https://example.com/example-package.git", revision: "aa681bd6c61e22df0fd808044a886fc4a7ed3a65"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `revision`: A dependency requirement. See static methods on   for available options.
- `traits`: The trait configuration of this dependency. Defaults to enabling the default traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:revision:traits:))*