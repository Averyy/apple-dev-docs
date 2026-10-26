---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/testtarget/testcase/test/result-swift.enum"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.TestResult.TestTarget.TestCase.Test.Result

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The result of running a single test.

## Declaration

```swift
enum Result
```

## Topics

### Test Results
- [PackageManager.TestResult.TestTarget.TestCase.Test.Result.succeeded](./result-swift.enum/succeeded.md)
- [PackageManager.TestResult.TestTarget.TestCase.Test.Result.skipped](./result-swift.enum/skipped.md)
- [PackageManager.TestResult.TestTarget.TestCase.Test.Result.failed](./result-swift.enum/failed.md)
### Creating a Test Result
- [init?(rawValue: String)](./result-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./result-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./result-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable

## See Also

### Inspecting a Test in a Test Case
- [var name: String](./name.md)
  The name of the test.
- [var result: Result](./result-swift.property.md)
  The test result.
- [var duration: Double](./duration.md)
  The duration of the test.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testresult/testtarget/testcase/test/result-swift.enum)*