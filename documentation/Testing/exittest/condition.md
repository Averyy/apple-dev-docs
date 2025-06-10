# ExitTest.Condition

**Framework**: Swift Testing  
**Kind**: struct

The possible conditions under which an exit test will complete.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
struct Condition
```

## Mentions

- [Exit testing](exit-testing.md)

#### Overview

Values of this type are used to describe the conditions under which an exit test is expected to pass or fail by passing them to [`expect(processExitsWith:observing:_:sourceLocation:performing:)`](expect(processexitswith:observing:_:sourcelocation:performing:).md) or [`require(processExitsWith:observing:_:sourceLocation:performing:)`](require(processexitswith:observing:_:sourcelocation:performing:).md).

## Topics

### Successful exit conditions
- [static var success: ExitTest.Condition](exittest/condition/success.md)
  A condition that matches when a process exits normally.
### Failing exit conditions
- [static var failure: ExitTest.Condition](exittest/condition/failure.md)
  A condition that matches when a process exits abnormally
- [static func exitCode(CInt) -> ExitTest.Condition](exittest/condition/exitcode(_:).md)
  Creates a condition that matches when a process terminates with a given exit code.
- [static func signal(CInt) -> ExitTest.Condition](exittest/condition/signal(_:).md)
  Creates a condition that matches when a process exits with a given signal.
### Initializers
- [init(ExitStatus)](exittest/condition/init(_:).md)
  Initialize an instance of this type that matches the specified exit status.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/condition)*