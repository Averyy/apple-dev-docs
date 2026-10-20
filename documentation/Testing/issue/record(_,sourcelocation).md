# record(_:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Type Method

Records an issue that a test encounters while it’s running.

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

> **Deprecated**: Use record(_:severity:sourceLocation:) instead.

## Declaration

```swift
@discardableResult
static func record(_ comment: Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation) -> Issue
```

#### Return Value

The issue that was recorded.

#### Discussion

Use this function if, while running a test, an issue occurs that cannot be represented as an expectation (using the [`expect(_:_:sourceLocation:)`](../expect%28_,_,sourcelocation%29.md) or [`require(_:_:sourceLocation:)`](../require%28_,_,sourcelocation%29-5l63q.md) macros.)

## Parameters

- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which the issue should be attributed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/issue/record(_:sourcelocation:))*