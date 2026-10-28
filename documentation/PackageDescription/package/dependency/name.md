# name

**Framework**: PackageDescription  
**Kind**: property  
**Role**: Instance Property

The name of the dependency.

**Availability**:
- SwiftPM - Deprecated in 5.6

> **Deprecated**: use kind instead

## Declaration

```swift
var name: String? { get }
```

## Discussion

If the `name` is `nil`, Swift Package Manager deduces the dependency’s name from its package identity or Git URL.

## See Also

### Describing a Package Dependency
- [let kind: Package.Dependency.Kind](./kind-swift.property.md)
  A description of the package dependency.
- [Package.Dependency.Kind](./kind-swift.enum.md)
  The type of dependency.
- [struct Version](../../version.md)
  A version according to the semantic versioning specification.
- [var url: String?](./url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/name)*