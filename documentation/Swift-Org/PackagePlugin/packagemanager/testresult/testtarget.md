---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/testtarget"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.TestResult.TestTarget

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

The results of running some or all of the tests in a single test target.

## Declaration

```swift
struct TestTarget
```

## Topics

### Inspecting a Test Target
- [var name: String](./testtarget/name.md)
  The name of the target.
- [var testCases: [TestCase]](./testtarget/testcases.md)
  The test cases included in the target.
- [PackageManager.TestResult.TestTarget.TestCase](./testtarget/testcase.md)
  The results of running some or all of the tests in a single test case.

## See Also

### Inspecting Test Results
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the test run succeeded.
- [var testTargets: [TestTarget]](./testtargets.md)
  Results for all the test targets run.
- [var codeCoverageDataFileURL: URL?](./codecoveragedatafileurl.md)
  The file URL of a generated profile file to provide code coverage.
- [var codeCoverageDataFile: Path?](./codecoveragedatafile.md)
  The path of a generated profile file to provide code corage.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/testtarget)*