# require(processExitsWith:observing:_:sourceLocation:performing:)

**Framework**: Swift Testing  
**Kind**: macro

Check that an expression causes the process to terminate in a given fashion and throw an error if it did not.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
@discardableResult
@freestanding(expression) macro require(processExitsWith expectedExitCondition: ExitTest.Condition, observing observedValues: [any PartialKeyPath<ExitTest.Result> & Sendable] = [], _ comment: @autoclosure () -> Comment? = nil, sourceLocation: SourceLocation = #_sourceLocation, performing expression: @escaping () async throws -> Void) -> ExitTest.Result
```

## Mentions

- [Exit testing](exit-testing.md)

#### Return Value

An instance of [`ExitTest.Result`](exittest/result.md) describing the state of the exit test when it exited.

#### Overview

> **Note**: An instance of [`ExpectationFailedError`](expectationfailederror.md) if the exit condition of the child process does not equal `expectedExitCondition`.

Use this overload of `#require()` when an expression will cause the current process to terminate and the nature of that termination will determine if the test passes or fails. For example, to test that calling `fatalError()` causes a process to terminate:

```swift
try await #require(processExitsWith: .failure) {
  fatalError()
}
```

## Parameters

- `expectedExitCondition`: The expected exit condition.
- `observedValues`: An array of key paths representing results from within   the exit test that should be observed and returned by this macro. The    property is always returned.
- `comment`: A comment describing the expectation.
- `sourceLocation`: The source location to which recorded expectations and   issues should be attributed.
- `expression`: The expression to be evaluated.

## See Also

- [Exit testing](exit-testing.md)
  Use exit tests to test functionality that might cause a test process to exit.
- [macro expect(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result?](expect(processexitswith:observing:_:sourcelocation:performing:).md)
  Check that an expression causes the process to terminate in a given fashion.
- [enum ExitStatus](exitstatus.md)
  An enumeration describing possible status a process will report on exit.
- [struct ExitTest](exittest.md)
  A type describing an exit test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/require(processexitswith:observing:_:sourcelocation:performing:))*