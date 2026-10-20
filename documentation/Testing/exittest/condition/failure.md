# failure

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Type Property

A condition that matches when a process exits abnormally

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
static var failure: ExitTest.Condition { get }
```

## Mentions

- [Exit testing](../../exit-testing.md)

#### Discussion

This condition matches any exit code other than `EXIT_SUCCESS` or any signal that causes the process to exit.

## See Also

### Failing exit conditions
- [static func exitCode(CInt) -> ExitTest.Condition](./exitcode%28_%29.md)
  Creates a condition that matches when a process terminates with a given exit code.
- [static func signal(CInt) -> ExitTest.Condition](./signal%28_%29.md)
  Creates a condition that matches when a process exits with a given signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/condition/failure)*