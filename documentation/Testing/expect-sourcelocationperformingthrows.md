# expect(_:sourceLocation:performing:throws:)

**Framework**: Swift Testing  
**Kind**: macro

Check that an expression always throws an error matching some condition.

**Availability**:
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
@discardableResult
@freestanding(expression) macro expect<R>(_ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation, performing expression: () async throws -> R, throws errorMatcher: (any Error) async throws -> Bool) -> (any Error)?
```

#### Return Value

If the expectation passes, the error that was thrown by `expression`. If the expectation fails, the result is `nil`.

#### Overview

Use this overload of `#expect()` when the expression `expression` *should* throw an error, but the logic to determine if the error matches is complex:

```swift
#expect {
  FoodTruck.shared.engine.batteryLevel = 0
  try FoodTruck.shared.engine.start()
} throws: { error in
  return error == EngineFailureError.batteryDied
    || error == EngineFailureError.stillCharging
}
```

If `expression` does not throw an error, if it throws an error that is not matched by `errorMatcher`, or if `errorMatcher` throws an error (including the error passed to it), an [`Issue`](issue.md) is recorded for the test that is running in the current task. Any value returned by `expression` is discarded.

If the thrown error need only be an instance of a particular type, use [`expect(throws:_:sourceLocation:performing:)`](expect(throws:_:sourcelocation:performing:)-1hfms.md) instead. If the thrown error need only equal another instance of [`Error`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/error), use [`expect(throws:_:sourceLocation:performing:)`](expect(throws:_:sourcelocation:performing:)-7du1h.md) instead.

## Parameters

- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which recorded expectations and issues should be attributed.
- `expression`: The expression to be evaluated.
- `errorMatcher`: A closure to invoke when `expression` throws an error that indicates if it matched or not.

## See Also

- [Testing for errors in Swift code](testing-for-errors-in-swift-code.md)
  Ensure that your code handles errors in the way you expect.
- [macro expect<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](expect(throws:_:sourcelocation:performing:)-1hfms.md)
  Check that an expression always throws an error of a given type.
- [macro expect<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](expect(throws:_:sourcelocation:performing:)-7du1h.md)
  Check that an expression always throws a specific error.
- [macro require<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](require(throws:_:sourcelocation:performing:)-7n34r.md)
  Check that an expression always throws an error of a given type, and throw an error if it does not.
- [macro require<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](require(throws:_:sourcelocation:performing:)-4djuw.md)
- [macro require<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> any Error](require(_:sourcelocation:performing:throws:).md)
  Check that an expression always throws an error matching some condition, and throw an error if it does not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expect(_:sourcelocation:performing:throws:))*