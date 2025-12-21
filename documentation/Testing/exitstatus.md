# ExitStatus

**Framework**: Swift Testing  
**Kind**: enum

An enumeration describing possible status a process will report on exit.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
enum ExitStatus
```

#### Overview

You can convert an instance of this type to an instance of [`ExitTest.Condition`](exittest/condition.md) using [`init(_:)`](exittest/condition/init(_:).md). That value can then be used to describe the condition under which an exit test is expected to pass or fail by passing it to [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](expect(processexitswith:observing:_:sourcelocation:performing:).md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](require(processexitswith:observing:_:sourcelocation:performing:).md).

## Topics

### Enumeration Cases
- [ExitStatus.exitCode(_:)](exitstatus/exitcode(_:).md)
  The process exited with the given exit code.
- [ExitStatus.signal(_:)](exitstatus/signal(_:).md)
  The process exited with the given signal.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Exit testing](exit-testing.md)
  Use exit tests to test functionality that might cause a test process to exit.
- [macro expect(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result?](expect(processexitswith:observing:_:sourcelocation:performing:).md)
  Check that an expression causes the process to terminate in a given fashion.
- [macro require(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result](require(processexitswith:observing:_:sourcelocation:performing:).md)
  Check that an expression causes the process to terminate in a given fashion and throw an error if it did not.
- [struct ExitTest](exittest.md)
  A type describing an exit test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exitstatus)*