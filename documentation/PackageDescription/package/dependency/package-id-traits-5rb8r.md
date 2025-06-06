# package(id:_:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(id: String, _ range: Range<Version>, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
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
- `traits`: The trait configuration of this dependency. Defaults to enabling the default traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(id:_:traits:)-5rb8r)*