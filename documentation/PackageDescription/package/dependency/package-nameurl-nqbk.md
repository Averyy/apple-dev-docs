# package(name:url:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String, url: String, _ range: Range<Version>) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions `1.2.3`, `1.2.4`, `1.2.5`, but not `1.2.6`.

```swift
.package(url: "https://example.com/example-package.git", "1.2.3"..<"1.2.6"),
```

## Parameters

- `name`: The name of the package, or   to deduce it from the URL.
- `url`: The valid Git URL of the package.
- `range`: The custom version range requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:_:)-nqbk)*