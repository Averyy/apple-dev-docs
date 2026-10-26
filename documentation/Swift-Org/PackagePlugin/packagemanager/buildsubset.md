---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildsubset"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildSubset

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

Specifies a subset of package products and targets to build.

## Declaration

```swift
enum BuildSubset
```

## Topics

### Subsets of the Package
- [PackageManager.BuildSubset.product(_:)](./buildsubset/product%28_%29.md)
  Represents the product with the specified name.
- [PackageManager.BuildSubset.target(_:)](./buildsubset/target%28_%29.md)
  Represents the target with the specified name.
- [PackageManager.BuildSubset.all(includingTests:)](./buildsubset/all%28includingtests%29.md)
  Represents the subset consisting of all products and of either all targets or, if `includingTests` is false, non-test targets.

## See Also

### Building a Package
- [func build(BuildSubset, parameters: BuildParameters) throws -> BuildResult](./build%28_,parameters%29.md)
  Performs a build of all, or a subset, of products and targets in a package.
- [PackageManager.BuildParameters](./buildparameters.md)
  Parameters and options to apply during a build.
- [PackageManager.BuildResult](./buildresult.md)
  The results of running a build.
- [PackageManager.BuildConfiguration](./buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](./buildlogverbosity.md)
  The amount of detail to include in a build log.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildsubset)*