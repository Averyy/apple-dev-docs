# Version

**Framework**: PackageDescription  
**Kind**: struct

A version according to the semantic versioning specification.

## Declaration

```swift
struct Version
```

#### Overview

A package version consists of three integers separated by periods, for example `1.0.0`. It must conform to the semantic versioning standard in order to ensure that your package behaves in a predictable manner once developers update their package dependency to a newer version. To achieve predictability, the semantic versioning specification proposes a set of rules and requirements that dictate how version numbers are assigned and incremented. To learn more about the semantic versioning specification, visit [`Semantic Versioning 2.0.0`](https://developer.apple.comhttps://semver.org).

## Topics

### Creating a new version
- [init(Int, Int, Int, prereleaseIdentifiers: [String], buildMetadataIdentifiers: [String])](version/init(_:_:_:prereleaseidentifiers:buildmetadataidentifiers:).md)
  Initializes a version struct with the provided components of a semantic version.
### Inspecting a version
- [let major: Int](version/major.md)
  The major version according to the semantic versioning standard.
- [let minor: Int](version/minor.md)
  The minor version according to the semantic versioning standard.
- [let patch: Int](version/patch.md)
  The patch version according to the semantic versioning standard.
- [let prereleaseIdentifiers: [String]](version/prereleaseidentifiers.md)
  The pre-release identifier according to the semantic versioning standard, such as `-beta.1`.
- [let buildMetadataIdentifiers: [String]](version/buildmetadataidentifiers.md)
  The build metadata of this version according to the semantic versioning standard, such as a commit hash.
### Default Implementations
- [Comparable Implementations](version/comparable-implementations.md)
- [CustomStringConvertible Implementations](version/customstringconvertible-implementations.md)
- [Equatable Implementations](version/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](version/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](version/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](version/expressiblebyunicodescalarliteral-implementations.md)
- [LosslessStringConvertible Implementations](version/losslessstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [LosslessStringConvertible](../Swift/LosslessStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let kind: Package.Dependency.Kind](package/dependency/kind-swift.property.md)
  A description of the package dependency.
- [Package.Dependency.Kind](package/dependency/kind-swift.enum.md)
  The type of dependency.
- [var name: String?](package/dependency/name.md)
  The name of the dependency.
- [var url: String?](package/dependency/url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/version)*