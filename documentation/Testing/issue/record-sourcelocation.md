# record(_:_:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method

Record a new issue when a running test unexpectedly catches an error.

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
@discardableResult
static func record(_ error: any Error, _ comment: Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation) -> Issue
```

#### Return Value

The issue that was recorded.

#### Discussion

This function can be used if an unexpected error is caught while running a test and it should be treated as a test failure. If an error is thrown from a test function, it is automatically recorded as an issue and this function does not need to be used.

## Parameters

- `error`: The error that caused the issue.
- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which the issue should be   attributed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/record(_:_:sourcelocation:))*