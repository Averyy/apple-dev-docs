# Expectations and confirmations

**Framework**: Swift Testing

Check for expected values, outcomes, and asynchronous events in tests.

#### Overview

Use [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md) and [`require(_:_:sourceLocation:)`](require(_:_:sourcelocation:)-5l63q.md) macros to validate expected outcomes. To validate that an error is thrown, or  thrown, the testing library provides several overloads of the macros that you can use. For more information, see [`Testing for errors in Swift code`](testing-for-errors-in-swift-code.md).

Use a [`Confirmation`](confirmation.md) to confirm the occurrence of an asynchronous event that you can’t check directly using an expectation. For more information, see [`Testing asynchronous code`](testing-asynchronous-code.md).

##### Validate Your Codes Result

To validate that your code produces an expected value, use [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md). This macro captures the expression you pass, and provides detailed information when the code doesn’t satisfy the expectation.

```swift
@Test func calculatingOrderTotal() {
  let calculator = OrderCalculator()
  #expect(calculator.total(of: [3, 3]) == 7)
  // Prints "Expectation failed: (calculator.total(of: [3, 3]) → 6) == 7"
}
```

Your test keeps running after [`expect(_:_:sourceLocation:)`](expect(_:_:sourcelocation:).md) fails. To stop the test when the code doesn’t satisfy a requirement, use [`require(_:_:sourceLocation:)`](require(_:_:sourcelocation:)-5l63q.md) instead:

```swift
@Test func returningCustomerRemembersUsualOrder() throws {
  let customer = try #require(Customer(id: 123))
  // The test runner doesn't reach this line if the customer is nil.
  #expect(customer.usualOrder.countOfItems == 2)
}
```

[`require(_:_:sourceLocation:)`](require(_:_:sourcelocation:)-5l63q.md) throws an instance of [`ExpectationFailedError`](expectationfailederror.md) when your code fails to satisfy the requirement.

## Topics

### Checking expectations
- [macro expect(Bool, @autoclosure () -> Comment?, sourceLocation: SourceLocation)](expect(_:_:sourcelocation:).md)
  Check that an expectation has passed after a condition has been evaluated.
- [macro require(Bool, @autoclosure () -> Comment?, sourceLocation: SourceLocation)](require(_:_:sourcelocation:)-5l63q.md)
  Check that an expectation has passed after a condition has been evaluated and throw an error if it failed.
- [macro require<T>(T?, @autoclosure () -> Comment?, sourceLocation: SourceLocation) -> T](require(_:_:sourcelocation:)-6w9oo.md)
  Unwrap an optional value or, if it is `nil`, fail and throw an error.
### Checking that errors are thrown
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
- [macro require<R>(@autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> R, throws: (any Error) async throws -> Bool) -> any Error](require(_:sourcelocation:performing:throws:).md)
  Check that an expression always throws an error matching some condition, and throw an error if it does not.
### Checking how processes exit
- [Exit testing](exit-testing.md)
  Use exit tests to test functionality that might cause a test process to exit.
- [macro expect(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result?](expect(processexitswith:observing:_:sourcelocation:performing:).md)
  Check that an expression causes the process to terminate in a given fashion.
- [macro require(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result](require(processexitswith:observing:_:sourcelocation:performing:).md)
  Check that an expression causes the process to terminate in a given fashion and throw an error if it did not.
- [enum ExitStatus](exitstatus.md)
  An enumeration describing possible status a process will report on exit.
- [struct ExitTest](exittest.md)
  A type describing an exit test.
### Confirming that asynchronous events occur
- [Testing asynchronous code](testing-asynchronous-code.md)
  Validate whether your code causes expected events to happen.
- [func confirmation<R>(Comment?, expectedCount: Int, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, (Confirmation) async throws -> sending R) async rethrows -> R](confirmation(_:expectedcount:isolation:sourcelocation:_:)-5mqz2.md)
  Confirm that some event occurs during the invocation of a function.
- [func confirmation<R>(Comment?, expectedCount: some RangeExpression<Int> & Sendable & Sequence<Int>, isolation: isolated (any Actor)?, sourceLocation: SourceLocation, (Confirmation) async throws -> sending R) async rethrows -> R](confirmation(_:expectedcount:isolation:sourcelocation:_:)-l3il.md)
  Confirm that some event occurs during the invocation of a function.
- [struct Confirmation](confirmation.md)
  A type that can be used to confirm that an event occurs zero or more times.
### Retrieving information about checked expectations
- [struct Expectation](expectation.md)
  A type describing an expectation that has been evaluated.
- [struct ExpectationFailedError](expectationfailederror.md)
  A type describing an error thrown when an expectation fails during evaluation.
- [protocol CustomTestStringConvertible](customteststringconvertible.md)
  A protocol describing types with a custom string representation when presented as part of a test’s output.
### Representing source locations
- [struct SourceLocation](sourcelocation.md)
  A type representing a location in source code.

## See Also

- [Known issues](known-issues.md)
  Mark issues as known when running tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/expectations)*