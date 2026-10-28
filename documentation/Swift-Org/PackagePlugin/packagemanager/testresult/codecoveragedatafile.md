---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/codecoveragedatafile"
framework: "Swift-Org/PackagePlugin"
---

# codeCoverageDataFile

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The path of a generated profile file to provide code corage.

**Availability**:
- SwiftPM - Deprecated in 6.0 (renamed: codeCoverageDataFileURL)

## Declaration

```swift
var codeCoverageDataFile: Path? { get }
```

## Discussion

The `.profdata` file is suitable for processing using `llvm-cov`, if `enableCodeCoverage` was set in the test parameters.

## See Also

### Inspecting Test Results
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the test run succeeded.
- [var testTargets: [TestTarget]](./testtargets.md)
  Results for all the test targets run.
- [var codeCoverageDataFileURL: URL?](./codecoveragedatafileurl.md)
  The file URL of a generated profile file to provide code coverage.
- [PackageManager.TestResult.TestTarget](./testtarget.md)
  The results of running some or all of the tests in a single test target.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/codecoveragedatafile)*