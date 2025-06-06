# package(name:url:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency with a given version requirement.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String?, url: String, _ requirement: Package.Dependency.Requirement) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

## Parameters

- `name`: The name of the Swift package or   to deduce the name from the package’s Git URL.
- `url`: The valid Git URL of the package.
- `requirement`: A dependency requirement. See static methods on    for available options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:_:)-6k3na)*