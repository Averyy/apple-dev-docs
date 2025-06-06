# require(_:_:sourceLocation:)

**Framework**: Testing  
**Kind**: macro

Check that an expectation has passed after a condition has been evaluated and throw an error if it failed.

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
(expression) macro require(_ condition: Bool, _ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation)
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)
- [Testing for errors in Swift code](testing-for-errors-in-swift-code.md)

#### Overview

> **Note**: An instance of [`ExpectationFailedError`](expectationfailederror.md) if `condition` evaluates to `false`.

If `condition` evaluates to `false`, an [`Issue`](issue.md) is recorded for the test that is running in the current task and an instance of [`ExpectationFailedError`](expectationfailederror.md) is thrown.

## Parameters

- `condition`: The condition to be evaluated.
- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which recorded expectations and   issues should be attributed.

## See Also

- [macro expect(Bool, @autoclosure () -> Comment?, sourceLocation: SourceLocation)](expect(_:_:sourcelocation:).md)
  Check that an expectation has passed after a condition has been evaluated.
- [macro require<T>(T?, @autoclosure () -> Comment?, sourceLocation: SourceLocation) -> T](require(_:_:sourcelocation:)-6w9oo.md)
  Unwrap an optional value or, if it is `nil`, fail and throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/require(_:_:sourcelocation:)-5l63q)*