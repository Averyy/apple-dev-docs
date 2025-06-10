# require(throws:_:sourceLocation:performing:)

**Framework**: Swift Testing  
**Kind**: macro

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
@freestanding(expression) macro require<E, R>(throws error: E, _ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation, performing expression: () async throws -> R) -> E where E : Equatable, E : Error
```

#### Return Value

The instance of `E` that was thrown by `expression` and is equal to `error`.

#### Overview

> **Note**: An instance of [`ExpectationFailedError`](expectationfailederror.md) if `expression` does not throw a matching error. The error thrown by `expression` is not rethrown.

Use this overload of `#require()` when the expression `expression`  throw a specific error:

```swift
try #require(throws: EngineFailureError.batteryDied) {
  FoodTruck.shared.engine.batteryLevel = 0
  try FoodTruck.shared.engine.start()
}
```

If `expression` does not throw an error, or if it throws an error that is not equal to `error`, an [`Issue`](issue.md) is recorded for the test that is running in the current task and an instance of [`ExpectationFailedError`](expectationfailederror.md) is thrown. Any value returned by `expression` is discarded.

> **Note**: If you use this macro with a Swift compiler version lower than 6.1, it doesn’t return a value.

If the thrown error need only be an instance of a particular type, use [`require(throws:_:sourceLocation:performing:)`](require(throws:_:sourcelocation:performing:)-7n34r.md) instead.

## See Also

- [Testing for errors in Swift code](testing-for-errors-in-swift-code.md)
  Ensure that your code handles errors in the way you expect.
- [macro expect<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](expect(throws:_:sourcelocation:performing:)-1hfms.md)
  Check that an expression always throws an error of a given type.
- [macro expect<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](expect(throws:_:sourcelocation:performing:)-7du1h.md)
  Check that an expression always throws a specific error.
- [macro expect<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> (any Error)?](expect(_:sourcelocation:performing:throws:).md)
  Check that an expression always throws an error matching some condition.
- [macro require<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](require(throws:_:sourcelocation:performing:)-7n34r.md)
  Check that an expression always throws an error of a given type, and throw an error if it does not.
- [macro require<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> any Error](require(_:sourcelocation:performing:throws:).md)
  Check that an expression always throws an error matching some condition, and throw an error if it does not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/require(throws:_:sourcelocation:performing:)-4djuw)*