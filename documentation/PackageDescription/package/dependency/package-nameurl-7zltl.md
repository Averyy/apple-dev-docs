# package(name:url:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.

**Availability**:
- SwiftPM 5.2+

## Declaration

```swift
static func package(name: String, url: String, _ range: ClosedRange<Version>) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions 1.2.3, 1.2.4, 1.2.5, as well as 1.2.6.

```swift
.package(url: "https://example.com/example-package.git", "1.2.3"..."1.2.6"),
```

The following example allows the Swift Package Manager to pick versions between 1.0.0 and 2.0.0

```swift
.package(url: "https://example.com/example-package.git", .upToNextMajor(from: "1.0.0"),
```

The following example allows the Swift Package Manager to pick versions between 1.0.0 and 1.1.0

```swift
.package(url: "https://example.com/example-package.git", .upToNextMinor(from: "1.0.0"),
```

## Parameters

- `name`: The name of the package, or   to deduce it from the URL.
- `url`: The valid Git URL of the package.
- `range`: The closed version range requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(name:url:_:)-7zltl)*