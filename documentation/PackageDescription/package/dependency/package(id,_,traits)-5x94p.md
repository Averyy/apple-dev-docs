# package(id:_:traits:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(id: String, _ range: ClosedRange<Version>, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

## Return Value

A `Package.Dependency` instance.

## Discussion

The following example allows the Swift Package Manager to pick versions 1.2.3, 1.2.4, 1.2.5, as well as 1.2.6.

```swift
.package(id: "scope.name", "1.2.3"..."1.2.6"),
```

## Parameters

- `id`: The identity of the package.
- `range`: The closed version range requirement.
- `traits`: The trait configuration of this dependency. The default value enables the default traits of the package.

## See Also

### Creating a package dependency from a registry
- [static func package(id: String, from: Version) -> Package.Dependency](./package%28id,from%29.md)
  Adds a remote package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28id,from,traits%29.md)
  Adds a remote package dependency that uses the version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(id: String, Range<Version>) -> Package.Dependency](./package%28id,_%29-27raa.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, Range<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28id,_,traits%29-5rb8r.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(id: String, ClosedRange<Version>) -> Package.Dependency](./package%28id,_%29-6anr7.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(id: String, exact: Version) -> Package.Dependency](./package%28id,exact%29.md)
  Adds a remote package dependency with an exact version requirement.
- [static func package(id: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28id,exact,traits%29.md)
  Adds a remote package dependency with an exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(id:_:traits:)-5x94p)*