# package(name:url:revision:)

**Framework**: PackageDescription  
**Kind**: method

Adds a remote package dependency given a revision requirement.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func package(name: String, url: String, revision: String) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

```swift
.package(url: "https://example.com/example-package.git", revision: "aa681bd6c61e22df0fd808044a886fc4a7ed3a65"),
```

## Parameters

- `name`: The name of the package, or nil to deduce it from the URL.
- `url`: The valid Git URL of the package.
- `revision`: A dependency requirement. See static methods on   for available options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:revision:))*