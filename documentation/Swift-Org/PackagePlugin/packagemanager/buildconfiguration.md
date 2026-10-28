---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildconfiguration"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildConfiguration

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The configuration to use for the build.

## Declaration

```swift
enum BuildConfiguration
```

## Overview

The configuration affects optimization and generation of debug symbols.

## Topics

### Build Configurations
- [PackageManager.BuildConfiguration.inherit](./buildconfiguration/inherit.md)
- [PackageManager.BuildConfiguration.debug](./buildconfiguration/debug.md)
- [PackageManager.BuildConfiguration.release](./buildconfiguration/release.md)
### Creating a Build Configuration
- [init?(rawValue: String)](./buildconfiguration/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./buildconfiguration/equatable-implementations.md)
- [RawRepresentable Implementations](./buildconfiguration/rawrepresentable-implementations.md)

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
- [PackageManager.BuildLogVerbosity](./buildlogverbosity.md)
  The amount of detail to include in a build log.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildconfiguration)*