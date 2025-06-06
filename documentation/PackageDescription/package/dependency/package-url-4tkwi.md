# package(url:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency given a version requirement.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
static func package(url: String, _ requirement: Package.Dependency.Requirement) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

## Parameters

- `url`: The valid Git URL of the package.
- `requirement`: A dependency requirement. See static methods on   for available options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:_:)-4tkwi)*