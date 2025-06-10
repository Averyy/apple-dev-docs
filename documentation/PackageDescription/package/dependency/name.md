# name

**Framework**: PackageDescription  
**Kind**: property

The name of the dependency.

**Availability**:
- SwiftPM ?+

## Declaration

```swift
var name: String? { get }
```

#### Discussion

If the `name` is `nil`, Swift Package Manager deduces the dependency’s name from its package identity or Git URL.

## See Also

- [let kind: Package.Dependency.Kind](package/dependency/kind-swift.property.md)
  A description of the package dependency.
- [Package.Dependency.Kind](package/dependency/kind-swift.enum.md)
  The type of dependency.
- [struct Version](version.md)
  A version according to the semantic versioning specification.
- [var url: String?](package/dependency/url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/name)*