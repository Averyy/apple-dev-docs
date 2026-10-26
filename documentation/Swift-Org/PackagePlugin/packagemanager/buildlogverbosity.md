---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildlogverbosity"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildLogVerbosity

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The amount of detail to include in a build log.

## Declaration

```swift
enum BuildLogVerbosity
```

## Topics

### Verbosity Levels
- [PackageManager.BuildLogVerbosity.concise](./buildlogverbosity/concise.md)
- [PackageManager.BuildLogVerbosity.debug](./buildlogverbosity/debug.md)
- [PackageManager.BuildLogVerbosity.verbose](./buildlogverbosity/verbose.md)
### Creating a Verbosity Level
- [init?(rawValue: String)](./buildlogverbosity/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./buildlogverbosity/equatable-implementations.md)
- [RawRepresentable Implementations](./buildlogverbosity/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable

## See Also

### Building a Package
- [func build(BuildSubset, parameters: BuildParameters) throws -> BuildResult](./build%28_,parameters%29.md)
  Performs a build of all, or a subset, of products and targets in a package.
- [PackageManager.BuildSubset](./buildsubset.md)
  Specifies a subset of package products and targets to build.
- [PackageManager.BuildParameters](./buildparameters.md)
  Parameters and options to apply during a build.
- [PackageManager.BuildResult](./buildresult.md)
  The results of running a build.
- [PackageManager.BuildConfiguration](./buildconfiguration.md)
  The configuration to use for the build.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildlogverbosity)*