# package(url:_:traits:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func package(url: String, _ range: Range<Version>, traits: Set<Package.Dependency.Trait> = [.defaults]) -> Package.Dependency
```

## Return Value

A `Package.Dependency` instance.

## Discussion

The following example allows the Swift Package Manager to pick versions `1.2.3`, `1.2.4`, `1.2.5`, but not `1.2.6`.

```swift
.package(url: "https://example.com/example-package.git", "1.2.3"..<"1.2.6"),
```

## Parameters

- `url`: The valid Git URL of the package.
- `range`: The custom version range requirement.
- `traits`: The trait configuration of this dependency. The default value enables the default traits of the package.

## See Also

### Creating a package dependency from a URL
- [static func package(url: String, from: Version) -> Package.Dependency](./package%28url,from%29.md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, from: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28url,from,traits%29.md)
  Adds a remote package dependency with a version requirement, starting with the given minimum version, going up to the next major version.
- [static func package(url: String, Range<Version>) -> Package.Dependency](./package%28url,_%29-2ys47.md)
  Adds a remote package dependency starting with a specific minimum version, up to but not including a specified maximum version.
- [static func package(url: String, ClosedRange<Version>) -> Package.Dependency](./package%28url,_%29-1r6rc.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, ClosedRange<Version>, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28url,_,traits%29-mjzv.md)
  Adds a remote package dependency starting with a specific minimum version, going up to and including a specific maximum version.
- [static func package(url: String, branch: String) -> Package.Dependency](./package%28url,branch%29.md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(url: String, branch: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28url,branch,traits%29.md)
  Adds a remote package dependency with a branch requirement you provide.
- [static func package(url: String, revision: String) -> Package.Dependency](./package%28url,revision%29.md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, revision: String, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28url,revision,traits%29.md)
  Adds a remote package dependency with a specific revision requirement.
- [static func package(url: String, exact: Version) -> Package.Dependency](./package%28url,exact%29.md)
  Adds a remote package dependency that uses an exact version requirement.
- [static func package(url: String, exact: Version, traits: Set<Package.Dependency.Trait>) -> Package.Dependency](./package%28url,exact,traits%29.md)
  Adds a remote package dependency that uses an exact version requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/package(url:_:traits:)-5pt81)*