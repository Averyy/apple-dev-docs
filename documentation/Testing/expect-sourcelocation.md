# expect(_:_:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: macro

Check that an expectation has passed after a condition has been evaluated.

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
@freestanding
(expression) macro expect(_ condition: Bool, _ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation)
```

## Mentions

- [Testing for errors in Swift code](testing-for-errors-in-swift-code.md)
- [Migrating a test from XCTest](migratingfromxctest.md)

#### Overview

If `condition` evaluates to `false`, an [`Issue`](issue.md) is recorded for the test that is running in the current task.

## Parameters

- `condition`: The condition to be evaluated.
- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which recorded expectations and   issues should be attributed.

## See Also

- [macro require(Bool, @autoclosure () -> Comment?, sourceLocation: SourceLocation)](require(_:_:sourcelocation:)-5l63q.md)
  Check that an expectation has passed after a condition has been evaluated and throw an error if it failed.
- [macro require<T>(T?, @autoclosure () -> Comment?, sourceLocation: SourceLocation) -> T](require(_:_:sourcelocation:)-6w9oo.md)
  Unwrap an optional value or, if it is `nil`, fail and throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expect(_:_:sourcelocation:))*