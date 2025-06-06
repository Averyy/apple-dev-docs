# package(id:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.

**Availability**:
- SwiftPM 5.7+

## Declaration

```swift
static func package(id: String, _ range: ClosedRange<Version>) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions 1.2.3, 1.2.4, 1.2.5, as well as 1.2.6.

```swift
.package(id: "scope.name", "1.2.3"..."1.2.6"),
```

## Parameters

- `id`: The identity of the package.
- `range`: The closed version range requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(id:_:)-6anr7)*