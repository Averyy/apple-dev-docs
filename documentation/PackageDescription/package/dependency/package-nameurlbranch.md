# package(name:url:branch:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency given a branch requirement.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func package(name: String, url: String, branch: String) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

```swift
.package(url: "https://example.com/example-package.git", branch: "main"),
```

## Parameters

- `name`: The name of the package, or nil to deduce it from the URL.
- `url`: The valid Git URL of the package.
- `branch`: A dependency requirement. See static methods on   for available options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:branch:))*