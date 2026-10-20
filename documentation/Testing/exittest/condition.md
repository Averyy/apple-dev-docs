# ExitTest.Condition

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

The possible conditions under which an exit test will complete.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
struct Condition
```

## Mentions

- [Exit testing](../exit-testing.md)

#### Overview

Values of this type are used to describe the conditions under which an exit test is expected to pass or fail by passing them to [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](../expect%28processexitswith,observing,_,sourcelocation,performing%29.md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](../require%28processexitswith,observing,_,sourcelocation,performing%29.md).

## Topics

### Successful exit conditions
- [static var success: ExitTest.Condition](./condition/success.md)
  A condition that matches when a process exits normally.
### Failing exit conditions
- [static var failure: ExitTest.Condition](./condition/failure.md)
  A condition that matches when a process exits abnormally
- [static func exitCode(CInt) -> ExitTest.Condition](./condition/exitcode%28_%29.md)
  Creates a condition that matches when a process terminates with a given exit code.
- [static func signal(CInt) -> ExitTest.Condition](./condition/signal%28_%29.md)
  Creates a condition that matches when a process exits with a given signal.
### Initializers
- [init(ExitStatus)](./condition/init%28_%29.md)
  Initialize an instance of this type that matches the specified exit status.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/condition)*