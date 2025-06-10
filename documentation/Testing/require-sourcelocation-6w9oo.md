# require(_:_:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: macro

Unwrap an optional value or, if it is `nil`, fail and throw an error.

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
(expression) macro require<T>(_ optionalValue: T?, _ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation) -> T
```

## Mentions

- [Migrating a test from XCTest](migratingfromxctest.md)

#### Return Value

The unwrapped value of `optionalValue`.

#### Overview

> **Note**: An instance of [`ExpectationFailedError`](expectationfailederror.md) if `optionalValue` is `nil`.

If `optionalValue` is `nil`, an [`Issue`](issue.md) is recorded for the test that is running in the current task and an instance of [`ExpectationFailedError`](expectationfailederror.md) is thrown.

## Parameters

- `optionalValue`: The optional value to be unwrapped.
- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which recorded expectations and   issues should be attributed.

## See Also

- [macro expect(Bool, @autoclosure () -> Comment?, sourceLocation: SourceLocation)](expect(_:_:sourcelocation:).md)
  Check that an expectation has passed after a condition has been evaluated.
- [macro require(Bool, @autoclosure () -> Comment?, sourceLocation: SourceLocation)](require(_:_:sourcelocation:)-5l63q.md)
  Check that an expectation has passed after a condition has been evaluated and throw an error if it failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/require(_:_:sourcelocation:)-6w9oo)*