# scopeProvider(for:testCase:)

**Framework**: Swift Testing  
**Kind**: method

Get this trait’s scope provider for the specified test or test case.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
func scopeProvider(for test: Test, testCase: Test.Case?) -> Never?
```

#### Discussion

The testing library uses this implementation of [`scopeProvider(for:testCase:)`](trait/scopeprovider(for:testcase:).md) when the trait type’s associated [`TestScopeProvider`](trait/testscopeprovider.md) type is `Never`.

## Parameters

- `test`: The test for which the testing library requests a   scope provider.
- `testCase`: The test case for which the testing library requests a scope   provider, if any. When   represents a suite, the value of this argument is   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/bug/scopeprovider(for:testcase:))*