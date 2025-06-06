# require(_:sourceLocation:performing:throws:)

**Framework**: Swift Testing  
**Kind**: macro

Check that an expression always throws an error matching some condition, and throw an error if it does not.

**Availability**:
- Swift 6.0+
- Xcode 16.0+

## Declaration

```swift
@discardableResult
@freestanding(expression) macro require<R>(_ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation, performing expression: () async throws -> R, throws errorMatcher: (any Error) async throws -> Bool) -> any Error
```

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
- [macro require<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](require(throws:_:sourcelocation:performing:)-4djuw.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/require(_:sourcelocation:performing:throws:))*