# expect(throws:_:sourceLocation:performing:)

**Framework**: Testing  
**Kind**: macro

Check that an expression always throws an error of a given type.

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
@freestanding(expression) macro expect<E, R>(throws errorType: E.Type, _ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation, performing expression: () async throws -> R) -> E? where E : Error
```

#### Return Value

If the expectation passes, the instance of `errorType` that was thrown by `expression`. If the expectation fails, the result is `nil`.

#### Overview

Use this overload of `#expect()` when the expression `expression`  throw an error of a given type:

```swift
#expect(throws: EngineFailureError.self) {
  FoodTruck.shared.engine.batteryLevel = 0
  try FoodTruck.shared.engine.start()
}
```

If `expression` does not throw an error, or if it throws an error that is not an instance of `errorType`, an [`Issue`](issue.md) is recorded for the test that is running in the current task. Any value returned by `expression` is discarded.

> **Note**: If you use this macro with a Swift compiler version lower than 6.1, it doesn’t return a value.

If the thrown error need only equal another instance of [`Error`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/error), use [`expect(throws:_:sourceLocation:performing:)`](expect(throws:_:sourcelocation:performing:)-7du1h.md) instead.

#### Expressions That Should Never Throw

If the expression `expression` should  throw any error, you can pass [`Never.self`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/never):

```swift
#expect(throws: Never.self) {
  FoodTruck.shared.engine.batteryLevel = 100
  try FoodTruck.shared.engine.start()
}
```

If `expression` throws an error, an [`Issue`](issue.md) is recorded for the test that is running in the current task. Any value returned by `expression` is discarded.

Test functions can be annotated with `throws` and can throw errors which are then recorded as issues when the test runs. If the intent is for a test to fail when an error is thrown by `expression`, rather than to explicitly check that an error is  thrown by it, do not use this macro. Instead, simply call the code in question and allow it to throw an error naturally.

## Parameters

- `errorType`: The type of error that is expected to be thrown. If    could throw   error, or the specific type of thrown   error is unimportant, pass  .
- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which recorded expectations and   issues should be attributed.
- `expression`: The expression to be evaluated.

## See Also

- [Testing for errors in Swift code](testing-for-errors-in-swift-code.md)
  Ensure that your code handles errors in the way you expect.
- [macro expect<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](expect(throws:_:sourcelocation:performing:)-7du1h.md)
  Check that an expression always throws a specific error.
- [macro expect<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> (any Error)?](expect(_:sourcelocation:performing:throws:).md)
  Check that an expression always throws an error matching some condition.
- [macro require<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](require(throws:_:sourcelocation:performing:)-7n34r.md)
  Check that an expression always throws an error of a given type, and throw an error if it does not.
- [macro require<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](require(throws:_:sourcelocation:performing:)-4djuw.md)
- [macro require<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> any Error](require(_:sourcelocation:performing:throws:).md)
  Check that an expression always throws an error matching some condition, and throw an error if it does not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expect(throws:_:sourcelocation:performing:)-1hfms)*