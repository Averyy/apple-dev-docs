# Package.Dependency.Kind

**Framework**: PackageDescription  
**Kind**: enum

The type of dependency.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [Package.Dependency.Kind.fileSystem(name:path:)](package/dependency/kind-swift.enum/filesystem(name:path:).md)
  A dependency located at the given path.
- [case registry(id: String, requirement: Package.Dependency.RegistryRequirement)](package/dependency/kind-swift.enum/registry(id:requirement:).md)
  A dependency based on a registry requirement.
- [case sourceControl(name: String?, location: String, requirement: Package.Dependency.SourceControlRequirement)](package/dependency/kind-swift.enum/sourcecontrol(name:location:requirement:).md)
  A dependency based on a source control requirement.

## See Also

- [let kind: Package.Dependency.Kind](package/dependency/kind-swift.property.md)
  A description of the package dependency.
- [struct Version](version.md)
  A version according to the semantic versioning specification.
- [var name: String?](package/dependency/name.md)
  The name of the dependency.
- [var url: String?](package/dependency/url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/kind-swift.enum)*