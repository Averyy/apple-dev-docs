---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testparameters"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.TestParameters

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Parameters that control how tests are run.

## Declaration

```swift
struct TestParameters
```

## Topics

### Creating Test Parameters
- [init(enableCodeCoverage: Bool)](./testparameters/init%28enablecodecoverage%29.md)
  Creates a new set of test parameters.
### Inspecting Test Parameters
- [var enableCodeCoverage: Bool](./testparameters/enablecodecoverage.md)
  Whether to collect code coverage information while running tests.

## See Also

### Testing a Package
- [func test(TestSubset, parameters: TestParameters) throws -> TestResult](./test%28_,parameters%29.md)
  Runs all, or a specified subset, of the unit tests of the package, after an incremental build if necessary.
- [PackageManager.TestSubset](./testsubset.md)
  Specifies which tests to run.
- [PackageManager.TestResult](./testresult.md)
  The result of running tests.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testparameters)*