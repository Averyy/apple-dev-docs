# Package.Dependency.Kind

**Framework**: PackageDescription  
**Kind**: enum  
**Role**: Enumeration

The type of dependency.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [Package.Dependency.Kind.fileSystem(name:path:)](./kind-swift.enum/filesystem%28name,path%29.md)
  A dependency located at the given path.
- [case registry(id: String, requirement: Package.Dependency.RegistryRequirement)](./kind-swift.enum/registry%28id,requirement%29.md)
  A dependency based on a registry requirement.
- [case sourceControl(name: String?, location: String, requirement: Package.Dependency.SourceControlRequirement)](./kind-swift.enum/sourcecontrol%28name,location,requirement%29.md)
  A dependency based on a source control requirement.

## See Also

### Describing a Package Dependency
- [let kind: Package.Dependency.Kind](./kind-swift.property.md)
  A description of the package dependency.
- [struct Version](../../version.md)
  A version according to the semantic versioning specification.
- [var name: String?](./name.md)
  The name of the dependency.
- [var url: String?](./url.md)
  The Git URL of the package dependency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/kind-swift.enum)*