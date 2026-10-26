---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Provides specialized information and services from the Swift Package Manager or an IDE that supports Swift packages.

## Declaration

```swift
struct PackageManager
```

#### Overview

Different plugin hosts implement the functionality in whatever way is appropriate for them, but are expected to preserve the semantics described by this API.

## Topics

### Building a Package
- [func build(BuildSubset, parameters: BuildParameters) throws -> BuildResult](./packagemanager/build%28_,parameters%29.md)
  Performs a build of all, or a subset, of products and targets in a package.
- [PackageManager.BuildSubset](./packagemanager/buildsubset.md)
  Specifies a subset of package products and targets to build.
- [PackageManager.BuildParameters](./packagemanager/buildparameters.md)
  Parameters and options to apply during a build.
- [PackageManager.BuildResult](./packagemanager/buildresult.md)
  The results of running a build.
- [PackageManager.BuildConfiguration](./packagemanager/buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](./packagemanager/buildlogverbosity.md)
  The amount of detail to include in a build log.
### Testing a Package
- [func test(TestSubset, parameters: TestParameters) throws -> TestResult](./packagemanager/test%28_,parameters%29.md)
  Runs all, or a specified subset, of the unit tests of the package, after an incremental build if necessary.
- [PackageManager.TestSubset](./packagemanager/testsubset.md)
  Specifies which tests to run.
- [PackageManager.TestParameters](./packagemanager/testparameters.md)
  Parameters that control how tests are run.
- [PackageManager.TestResult](./packagemanager/testresult.md)
  The result of running tests.
### Retrieving Symbols for a Package
- [func getSymbolGraph(for: Target, options: SymbolGraphOptions) throws -> SymbolGraphResult](./packagemanager/getsymbolgraph%28for,options%29.md)
  Return a directory containing symbol graph files for the given target and options.
- [PackageManager.SymbolGraphOptions](./packagemanager/symbolgraphoptions.md)
  Represents options for symbol graph generation.
- [PackageManager.SymbolGraphResult](./packagemanager/symbolgraphresult.md)
  The result of symbol graph generation.

## See Also

### Interacting with Package Manager
- [enum PackageManagerProxyError](./packagemanagerproxyerror.md)
  Errors from methods using the package manager.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager)*