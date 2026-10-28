# ExitStatus

**Framework**: Swift Testing  
**Kind**: enum  
**Role**: Enumeration

An enumeration describing possible status a process will report on exit.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
enum ExitStatus
```

## Overview

You can convert an instance of this type to an instance of [`ExitTest.Condition`](./exittest/condition.md) using [`init(_:)`](./exittest/condition/init%28_%29.md). That value can then be used to describe the condition under which an exit test is expected to pass or fail by passing it to [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](./expect%28processexitswith,observing,_,sourcelocation,performing%29.md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](./require%28processexitswith,observing,_,sourcelocation,performing%29.md).

## Topics

### Enumeration Cases
- [ExitStatus.exitCode(_:)](./exitstatus/exitcode%28_%29.md)
  The process exited with the given exit code.
- [ExitStatus.signal(_:)](./exitstatus/signal%28_%29.md)
  The process exited with the given signal.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking how processes exit
- [Exit testing](./exit-testing.md)
  Use exit tests to test functionality that might cause a test process to exit.
- [macro expect(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result?](./expect%28processexitswith,observing,_,sourcelocation,performing%29.md)
  Check that an expression causes the process to terminate in a given fashion.
- [macro require(processExitsWith: ExitTest.Condition, observing: [any PartialKeyPath<ExitTest.Result> & Sendable], @autoclosure () -> Comment?, sourceLocation: SourceLocation, performing: () async throws -> Void) -> ExitTest.Result](./require%28processexitswith,observing,_,sourcelocation,performing%29.md)
  Check that an expression causes the process to terminate in a given fashion and throw an error if it did not.
- [struct ExitTest](./exittest.md)
  A type describing an exit test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exitstatus)*