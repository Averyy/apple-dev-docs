# prepare(for:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prepare to run the test that has this trait.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
func prepare(for test: Test) async throws
```

#### Discussion

> **Throws**: Any error that prevents the test from running. If an error is thrown from this method, the test is skipped and the error is recorded as an [`Issue`](../issue.md).

The testing library calls this method after it discovers all tests and their traits, and before it begins to run any tests. Use this method to prepare necessary internal state, or to determine whether the test should run.

The default implementation of this method does nothing.

## Parameters

- `test`: The test that has this trait.

## Default Implementations

### Trait Implementations
- [func prepare(for: Test) async throws](./prepare%28for%29-4pe01.md)
  Prepare to run the test that has this trait.

## See Also

### Running code before and after a test or suite
- [protocol TestScoping](../testscoping.md)
  A protocol that tells the test runner to run custom code before or after it runs a test suite or test function.
- [func scopeProvider(for: Test, testCase: Test.Case?) -> Self.TestScopeProvider?](./scopeprovider%28for,testcase%29.md)
  Get this trait’s scope provider for the specified test and optional test case.
- [associatedtype TestScopeProvider : TestScoping = Never](./testscopeprovider.md)
  The type of the test scope provider for this trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/prepare(for:))*