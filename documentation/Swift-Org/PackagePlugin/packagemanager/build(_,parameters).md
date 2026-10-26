---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/build(_:parameters:)"
framework: "Swift-Org/PackagePlugin"
---

# build(_:parameters:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Performs a build of all, or a subset, of products and targets in a package.

## Declaration

```swift
func build(_ subset: BuildSubset, parameters: BuildParameters) throws -> BuildResult
```

#### Return Value

The build results.

#### Discussion

Return any errors encountered during the build in the build result, as well as the log of the build commands that it runs. This method throws an error if the input parameters are invalid, or in case the build can’t be started.

The Swift package manager command line interface or any IDE that supports packages may show the progress of the build as it happens.

## Parameters

- `subset`: The subset of targets to build.
- `parameters`: The build parameters to apply.

## See Also

### Building a Package
- [PackageManager.BuildSubset](./buildsubset.md)
  Specifies a subset of package products and targets to build.
- [PackageManager.BuildParameters](./buildparameters.md)
  Parameters and options to apply during a build.
- [PackageManager.BuildResult](./buildresult.md)
  The results of running a build.
- [PackageManager.BuildConfiguration](./buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](./buildlogverbosity.md)
  The amount of detail to include in a build log.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/build(_:parameters:))*