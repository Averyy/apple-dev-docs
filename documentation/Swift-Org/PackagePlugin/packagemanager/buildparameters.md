---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildParameters

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Parameters and options to apply during a build.

## Declaration

```swift
struct BuildParameters
```

## Topics

### Creating Build Parameters
- [init(configuration: BuildConfiguration, logging: BuildLogVerbosity, echoLogs: Bool)](./buildparameters/init%28configuration,logging,echologs%29.md)
  Creates a new sert of build parameters.
- [PackageManager.BuildConfiguration](./buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](./buildlogverbosity.md)
  The amount of detail to include in a build log.
### Inspecting Build Parameters
- [var configuration: BuildConfiguration](./buildparameters/configuration.md)
  The build configuration to use while building.
- [var logging: BuildLogVerbosity](./buildparameters/logging.md)
  Controls the amount of detail in the log returned in the build result.
- [var echoLogs: Bool](./buildparameters/echologs.md)
  A Boolean value that indicates whether to print build logs to the console.
- [var otherCFlags: [String]](./buildparameters/othercflags.md)
  Additional flags to pass to all C compiler invocations for the destination platform.
- [var otherCxxFlags: [String]](./buildparameters/othercxxflags.md)
  Additional flags to pass to all C++ compiler invocations for the destination platform.
- [var otherLinkerFlags: [String]](./buildparameters/otherlinkerflags.md)
  Additional flags to pass to all linker invocations for the destination platform.
- [var otherSwiftcFlags: [String]](./buildparameters/otherswiftcflags.md)
  Additional flags to pass to all Swift compiler invocations for the destination platform.

## See Also

### Building a Package
- [func build(BuildSubset, parameters: BuildParameters) throws -> BuildResult](./build%28_,parameters%29.md)
  Performs a build of all, or a subset, of products and targets in a package.
- [PackageManager.BuildSubset](./buildsubset.md)
  Specifies a subset of package products and targets to build.
- [PackageManager.BuildResult](./buildresult.md)
  The results of running a build.
- [PackageManager.BuildConfiguration](./buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](./buildlogverbosity.md)
  The amount of detail to include in a build log.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildparameters)*