---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.TestResult

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

The result of running tests.

## Declaration

```swift
struct TestResult
```

## Topics

### Inspecting Test Results
- [var succeeded: Bool](./testresult/succeeded.md)
  A Boolean value that indicates whether the test run succeeded.
- [var testTargets: [TestTarget]](./testresult/testtargets.md)
  Results for all the test targets run.
- [var codeCoverageDataFileURL: URL?](./testresult/codecoveragedatafileurl.md)
  The file URL of a generated profile file to provide code coverage.
- [PackageManager.TestResult.TestTarget](./testresult/testtarget.md)
  The results of running some or all of the tests in a single test target.
- [var codeCoverageDataFile: Path?](./testresult/codecoveragedatafile.md)
  The path of a generated profile file to provide code corage.

## See Also

### Testing a Package
- [func test(TestSubset, parameters: TestParameters) throws -> TestResult](./test%28_,parameters%29.md)
  Runs all, or a specified subset, of the unit tests of the package, after an incremental build if necessary.
- [PackageManager.TestSubset](./testsubset.md)
  Specifies which tests to run.
- [PackageManager.TestParameters](./testparameters.md)
  Parameters that control how tests are run.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult)*