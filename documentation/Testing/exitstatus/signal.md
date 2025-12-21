# ExitStatus.signal(_:)

**Framework**: Swift Testing  
**Kind**: case

The process exited with the given signal.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
case signal(CInt)
```

#### Discussion

The C programming language defines a number of standard signals. Platforms may additionally define their own non-standard signal codes:

| Platform | Header |
| --- | --- |
| macOS | [`<signal.h>`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/signal.3.html) |
| Linux | [`<signal.h>`](https://developer.apple.comhttps://www.kernel.org/doc/man-pages/online/pages/man7/signal.7.html) |
| FreeBSD | [`<signal.h>`](https://developer.apple.comhttps://man.freebsd.org/cgi/man.cgi?signal(3)) |
| OpenBSD | [`<signal.h>`](https://developer.apple.comhttps://man.openbsd.org/signal.3) |
| Windows | [`<signal.h>`](https://developer.apple.comhttps://learn.microsoft.com/en-us/cpp/c-runtime-library/signal-constants) |

## Parameters

- `signal`: The signal that caused the process to exit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exitstatus/signal(_:))*