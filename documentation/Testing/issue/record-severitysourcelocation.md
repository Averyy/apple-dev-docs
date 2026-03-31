# record(_:severity:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method

Records an issue that a test encounters while it’s running.

**Availability**:
- Swift 6.3+
- Xcode 26.4+ (Beta)

## Declaration

```swift
@discardableResult
static func record(_ comment: Comment? = nil, severity: Issue.Severity = .error, sourceLocation: SourceLocation = #_sourceLocation) -> Issue
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Return Value

The issue that was recorded.

#### Discussion

Use this function if, while running a test, an issue occurs that cannot be represented as an expectation (using the [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md) or [`require(_:_:sourceLocation:)`](require(_:_:sourcelocation:)-5l63q.md) macros.)

## Parameters

- `comment`: A comment describing the expectation.
- `severity`: The severity level of the issue.  The testing library marks the test as failed if the severity is greater than [`Issue.Severity.warning`](issue/severity-swift.enum/warning.md). The default is [`Issue.Severity.error`](issue/severity-swift.enum/error.md).
- `sourceLocation`: The source location to which the issue should be attributed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/record(_:severity:sourcelocation:))*