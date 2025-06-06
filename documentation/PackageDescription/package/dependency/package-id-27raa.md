# package(id:_:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.

**Availability**:
- SwiftPM 5.7+

## Declaration

```swift
static func package(id: String, _ range: Range<Version>) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

The following example allows the Swift Package Manager to pick versions `1.2.3`, `1.2.4`, `1.2.5`, but not `1.2.6`.

```swift
.package(id: "scope.name", "1.2.3"..<"1.2.6"),
```

The following example allows the Swift Package Manager to pick versions between 1.0.0 and 2.0.0

```swift
.package(id: "scope.name", .upToNextMajor(from: "1.0.0"),
```

The following example allows the Swift Package Manager to pick versions between 1.0.0 and 1.1.0

```swift
.package(id: "scope.name", .upToNextMinor(from: "1.0.0"),
```

## Parameters

- `id`: The identity of the package.
- `range`: The custom version range requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(id:_:)-27raa)*