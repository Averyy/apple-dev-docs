# package(id:exact:traits:)

**Framework**: PackageDescription  
**Kind**: method

Adds a package dependency that uses the exact version requirement.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(id: String, exact version: Version, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

#### Return Value

A `Package.Dependency` instance.

#### Discussion

Specifying exact version requirements are not recommended as they can cause conflicts in your dependency graph when multiple other packages depend on a package. Because Swift packages follow the semantic versioning convention, think about specifying a version range instead.

The following example instructs the Swift Package Manager to use version `1.2.3`.

```swift
.package(id: "scope.name", exact: "1.2.3"),
```

## Parameters

- `id`: The identity of the package.
- `version`: The exact version of the dependency for this requirement.
- `traits`: The trait configuration of this dependency. Defaults to enabling the default traits.

## See Also

- [static func package(id: String, from: Version) -> Package.Dependency](package/dependency/package(id:from:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:from:traits:).md)
  Adds a package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, Range<Version>) -> Package.Dependency](package/dependency/package(id:_:)-27raa.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:_:traits:)-5rb8r.md)
  Adds a package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, ClosedRange<Version>) -> Package.Dependency](package/dependency/package(id:_:)-6anr7.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](package/dependency/package(id:_:traits:)-5x94p.md)
  Adds a package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, exact: Version) -> Package.Dependency](package/dependency/package(id:exact:).md)
  Adds a package dependency that uses the exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(id:exact:traits:))*