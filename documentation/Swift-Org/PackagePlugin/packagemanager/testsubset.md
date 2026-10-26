---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testsubset"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.TestSubset

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

Specifies which tests to run.

## Declaration

```swift
enum TestSubset
```

## Topics

### Subsets of Tests
- [PackageManager.TestSubset.all](./testsubset/all.md)
  All tests in the package.
- [PackageManager.TestSubset.filtered(_:)](./testsubset/filtered%28_%29.md)
  One or more tests filtered by regular expression. Use the format `<test-target>.<test-case>` or `<test-target>.<test-case>/<test>`.

## See Also

### Testing a Package
- [func test(TestSubset, parameters: TestParameters) throws -> TestResult](./test%28_,parameters%29.md)
  Runs all, or a specified subset, of the unit tests of the package, after an incremental build if necessary.
- [PackageManager.TestParameters](./testparameters.md)
  Parameters that control how tests are run.
- [PackageManager.TestResult](./testresult.md)
  The result of running tests.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/testsubset)*