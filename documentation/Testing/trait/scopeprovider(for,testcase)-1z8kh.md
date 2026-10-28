# scopeProvider(for:testCase:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Instance Method

Get this trait’s scope provider for the specified test or test case.

**Availability**:
- Swift 6.1+
- Xcode 16.3+

## Declaration

```swift
func scopeProvider(for test: Test, testCase: Test.Case?) -> Self?
```

Available when `Self` conforms to `TestScoping`.

## Discussion

The testing library uses this implementation of [`scopeProvider(for:testCase:)`](./scopeprovider%28for,testcase%29.md) when the trait type conforms to [`TestScoping`](../testscoping.md).

## Parameters

- `test`: The test for which the testing library requests a scope provider.
- `testCase`: The test case for which the testing library requests a scope provider, if any. When `test` represents a suite, the value of this argument is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/trait/scopeprovider(for:testcase:)-1z8kh)*