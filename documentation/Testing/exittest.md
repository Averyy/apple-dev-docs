# ExitTest

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

A type describing an exit test.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
struct ExitTest
```

## Overview

Instances of this type describe exit tests you create using the [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](./expect%28processexitswith,observing,_,sourcelocation,performing%29.md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](./require%28processexitswith,observing,_,sourcelocation,performing%29.md) macro. You don’t usually need to interact directly with an instance of this type.

## Topics

### Structures
- [ExitTest.Condition](./exittest/condition.md)
  The possible conditions under which an exit test will complete.
- [ExitTest.Result](./exittest/result.md)
  A type representing the result of an exit test after it has exited and returned control to the calling test function.
### Type Properties
- [static var current: ExitTest?](./exittest/current.md)
  The exit test that is running in the current process, if any.

## Relationships

### Conforms To
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
- [enum ExitStatus](./exitstatus.md)
  An enumeration describing possible status a process will report on exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest)*