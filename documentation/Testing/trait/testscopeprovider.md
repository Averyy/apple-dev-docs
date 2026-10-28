# TestScopeProvider

**Framework**: Swift Testing  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type of the test scope provider for this trait.

**Availability**:
- Swift 6.1+
- Xcode 16.3+

## Declaration

```swift
associatedtype TestScopeProvider : TestScoping = Never
```

## Discussion

The default type is `Never`, which can’t be instantiated. The [`scopeProvider(for:testCase:)`](./scopeprovider%28for,testcase%29.md) method for any trait with `Never` as its test scope provider type must return `nil`, meaning that the trait doesn’t provide a custom scope for tests it’s applied to.

## See Also

### Running code before and after a test or suite
- [protocol TestScoping](../testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Self.TestScopeProvider?](./scopeprovider%28for,testcase%29.md)
  Get this trait’s scope provider for the specified test and optional test case.
- [func prepare(for: Test) async throws](./prepare%28for%29.md)
  Prepare to run the test that has this trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/testscopeprovider)*