# failure

**Framework**: Swift Testing  
**Kind**: property

A condition that matches when a process exits abnormally

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
static var failure: ExitTest.Condition { get }
```

## Mentions

- [Exit testing](exit-testing.md)

#### Discussion

This condition matches any exit code other than `EXIT_SUCCESS` or any signal that causes the process to exit.

## See Also

- [static func exitCode(CInt) -> ExitTest.Condition](exittest/condition/exitcode(_:).md)
  Creates a condition that matches when a process terminates with a given exit code.
- [static func signal(CInt) -> ExitTest.Condition](exittest/condition/signal(_:).md)
  Creates a condition that matches when a process exits with a given signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/condition/failure)*