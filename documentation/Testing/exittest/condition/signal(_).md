# signal(_:)

**Framework**: Swift Testing  
**Kind**: method  
**Role**: Type Method

Creates a condition that matches when a process exits with a given signal.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
static func signal(_ signal: CInt) -> ExitTest.Condition
```

## Mentions

- [Exit testing](../../exit-testing.md)

## Discussion

The C programming language defines a number of standard signals. Platforms may additionally define their own non-standard signal codes:

| Platform | Header |
| --- | --- |
| macOS | [<signal.h>](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/signal.3.html) |
| Linux | [<signal.h>](https://www.kernel.org/doc/man-pages/online/pages/man7/signal.7.html) |
| FreeBSD | [<signal.h>](https://man.freebsd.org/cgi/man.cgi?signal(3)) |
| OpenBSD | [<signal.h>](https://man.openbsd.org/signal.3) |
| Windows | [<signal.h>](https://learn.microsoft.com/en-us/cpp/c-runtime-library/signal-constants) |

## Parameters

- `signal`: The signal that caused the process to exit.

## See Also

### Failing exit conditions
- [static var failure: ExitTest.Condition](./failure.md)
  A condition that matches when a process exits abnormally
- [static func exitCode(CInt) -> ExitTest.Condition](./exitcode%28_%29.md)
  Creates a condition that matches when a process terminates with a given exit code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exittest/condition/signal(_:))*