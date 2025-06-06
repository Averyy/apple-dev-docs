# package(url:_:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, _ range: ClosedRange<Version>, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions 1.2.3, 1.2.4, 1.2.5, as well as 1.2.6.

```swift
.package(url: "https://example.com/example-package.git", "1.2.3"..."1.2.6"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `range`: The closed version range requirement.
- `traits`: The trait configuration of this dependency. Defaults to enabling the default traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:_:traits:)-mjzv)*