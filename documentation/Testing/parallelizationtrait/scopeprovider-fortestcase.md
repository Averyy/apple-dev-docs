# scopeProvider(for:testCase:)

**Framework**: Swift Testing  
**Kind**: method

Get this trait’s scope provider for the specified test and optional test case.

**Availability**:
- Swift 6.1+
- Xcode 16.3+

## Declaration

```swift
func scopeProvider(for test: Test, testCase: Test.Case?) -> Self?
```

#### Discussion

The testing library uses this implementation of [`scopeProvider(for:testCase:)`](trait/scopeprovider(for:testcase:).md) when the trait type conforms to both [`SuiteTrait`](suitetrait.md) and [`TestScoping`](testscoping.md).

## Parameters

- `test`: The test for which the testing library requests a scope   provider.
- `testCase`: The test case for which the testing library requests a scope   provider, if any. When   represents a suite, the value of this   argument is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/parallelizationtrait/scopeprovider(for:testcase:))*