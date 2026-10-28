---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/test(_:parameters:)"
framework: "Swift-Org/PackagePlugin"
---

# test(_:parameters:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Runs all, or a specified subset, of the unit tests of the package, after an incremental build if necessary.

## Declaration

```swift
func test(_ subset: TestSubset, parameters: TestParameters) throws -> TestResult
```

## Return Value

The test results.

## Discussion

The is functionally the same as `swift test` on the command line.

The returned test result includes any test failures. This method throws an error if the input parameters are invalid, or if the test cannot be started.

The Swift package manager command-line interface, or any IDE, may show the progress of the tests as they happen.

## Parameters

- `subset`: The subset of tests to run.
- `parameters`: The test parameters to apply.

## See Also

### Testing a Package
- [PackageManager.TestSubset](./testsubset.md)
  Specifies which tests to run.
- [PackageManager.TestParameters](./testparameters.md)
  Parameters that control how tests are run.
- [PackageManager.TestResult](./testresult.md)
  The result of running tests.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/test(_:parameters:))*