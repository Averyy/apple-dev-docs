# Testing for errors in Swift code

**Framework**: Swift Testing  
**Role**: Article

Ensure that your code handles errors in the way you expect.

## Overview

Write tests for your code that validate the conditions in which the code throws errors, and the conditions in which it returns without throwing an error. Use overloads of the [`expect(_:_:sourceLocation:)`](./expect%28_,_,sourcelocation%29.md) and [`require(_:_:sourceLocation:)`](./require%28_,_,sourcelocation%29-5l63q.md) macros that check for errors.

### Validate that your code throws an expected error

Create a test function that `throws` and `try` the code under test. If the code throws an error, then your test fails.

To check that the code under test throws a specific error, or to continue a longer test function after the code throws an error, pass that error as the first argument of [`expect(throws:_:sourceLocation:performing:)`](./expect%28throws,_,sourcelocation,performing%29-7du1h.md), and pass a closure that calls the code under test:

```swift
@Test func cannotAddToppingToPizzaBeforeStartOfList() {
  var order = PizzaToppings(bases: [.calzone, .deepCrust])
  #expect(throws: PizzaToppings.Error.outOfRange) {
    try order.add(topping: .mozarella, toPizzasIn: -1..<0)
  }
}
```

If the closure completes without throwing an error, the testing library records an issue. Other overloads of [`expect(_:_:sourceLocation:)`](./expect%28_,_,sourcelocation%29.md) let you test that the code throws an error of a given type, or matches an arbitrary Boolean test. Similar overloads of [`require(_:_:sourceLocation:)`](./require%28_,_,sourcelocation%29-5l63q.md) stop running your test if the code doesn’t throw the expected error.

### Validate that your code throws any error

To check that the code under test throws an error of any type, pass `(any Error).self` as the first argument to either [`expect(throws:_:sourceLocation:performing:)`](./expect%28throws,_,sourcelocation,performing%29-1hfms.md) or [`require(throws:_:sourceLocation:performing:)`](./require%28throws,_,sourcelocation,performing%29-7n34r.md):

```swift
@Test func cannotAddToppingToPizzaBeforeStartOfList() {
  var order = PizzaToppings(bases: [.calzone, .deepCrust])
  #expect(throws: (any Error).self) {
    try order.add(topping: .mozarella, toPizzasIn: -1..<0)
  }
}
```

### Validate that your code doesn’t throw an error

A test function that throws an error fails, which is usually sufficient for testing that the code under test doesn’t throw. If you need to record a thrown error as an issue without stopping the test function, compare the error to `Never`:

```swift
@Test func canAddToppingToPizzaInPositionZero() throws {
  var order = PizzaToppings(bases: [.thinCrust, .thinCrust])
  #expect(throws: Never.self) {
    try order.add(topping: .caper, toPizzasIn: 0..<1)
  }
  let toppings = try order.toppings(forPizzaAt: 0)
  #expect(toppings == [.caper])
}
```

If the closure throws *any* error, the testing library records an issue. If you need the test to stop when the code throws an error, include the code inline in the test function instead of wrapping it in a call to [`expect(throws:_:sourceLocation:performing:)`](./expect%28throws,_,sourcelocation,performing%29-7du1h.md).

## Inspect an error thrown by your code

When you use `#expect(throws:)` or `#require(throws:)` and the error matches the expectation, it is returned to the caller so that you can perform additional validation. If the expectation fails because no error was thrown or an error of a different type was thrown, `#expect(throws:)` returns `nil`:

```swift
@Test func cannotAddMarshmallowsToPizza() throws {
  let error = #expect(throws: PizzaToppings.InvalidToppingError.self) {
    try Pizza.current.add(topping: .marshmallows)
  }
  #expect(error?.topping == .marshmallows)
  #expect(error?.reason == .dessertToppingOnly)
}
```

If you aren’t sure what type of error will be thrown, pass `(any Error).self`.

## See Also

### Checking that errors are thrown
- [macro expect<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](./expect%28throws,_,sourcelocation,performing%29-1hfms.md)
  Check that an expression always throws an error of a given type.
- [macro expect<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E?](./expect%28throws,_,sourcelocation,performing%29-7du1h.md)
  Check that an expression always throws a specific error.
- [macro expect<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> (any Error)?](./expect%28_,sourcelocation,performing,throws%29.md)
  Check that an expression always throws an error matching some condition.
- [macro require<E, R>(throws: E.Type, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](./require%28throws,_,sourcelocation,performing%29-7n34r.md)
  Check that an expression always throws an error of a given type, and throw an error if it does not.
- [macro require<E, R>(throws: E, @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R) -> E](./require%28throws,_,sourcelocation,performing%29-4djuw.md)
- [macro require<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> any Error](./require%28_,sourcelocation,performing,throws%29.md)
  Check that an expression always throws an error matching some condition, and throw an error if it does not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/testing-for-errors-in-swift-code)*