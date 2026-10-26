---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/codecoveragedatafileurl"
framework: "Swift-Org/PackagePlugin"
---

# codeCoverageDataFileURL

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The file URL of a generated profile file to provide code coverage.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
var codeCoverageDataFileURL: URL?
```

#### Discussion

The `.profdata` file is suitable for processing using `llvm-cov`, if `enableCodeCoverage` was set in the test parameters.

## See Also

### Inspecting Test Results
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the test run succeeded.
- [var testTargets: [TestTarget]](./testtargets.md)
  Results for all the test targets run.
- [PackageManager.TestResult.TestTarget](./testtarget.md)
  The results of running some or all of the tests in a single test target.
- [var codeCoverageDataFile: Path?](./codecoveragedatafile.md)
  The path of a generated profile file to provide code corage.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/codecoveragedatafileurl)*