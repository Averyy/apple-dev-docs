# prepare(for:)

**Framework**: Testing  
**Kind**: method

Prepare to run the test that has this trait.

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
func prepare(for test: Test) async throws
```

#### Discussion

> **Note**: Any error that prevents the test from running. If an error is thrown from this method, the test is skipped and the error is recorded as an [`Issue`](issue.md).

The testing library calls this method after it discovers all tests and their traits, and before it begins to run any tests. Use this method to prepare necessary internal state, or to determine whether the test should run.

The default implementation of this method does nothing.

## Parameters

- `test`: The test that has this trait.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/conditiontrait/prepare(for:))*