# ExitStatus.exitCode(_:)

**Framework**: Swift Testing  
**Kind**: case

The process exited with the given exit code.

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
case exitCode(CInt)
```

#### Discussion

The C programming language defines two standard exit codes, `EXIT_SUCCESS` and `EXIT_FAILURE`. Platforms may additionally define their own non-standard exit codes:

| Platform | Header |
| --- | --- |
| macOS | [`<stdlib.h>`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/_Exit.3.html), [`<sysexits.h>`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysexits.3.html) |
| Linux | [`<stdlib.h>`](https://developer.apple.comhttps://www.kernel.org/doc/man-pages/online/pages/man3/exit.3.html), [`<sysexits.h>`](https://developer.apple.comhttps://www.kernel.org/doc/man-pages/online/pages/man3/sysexits.h.3head.html) |
| FreeBSD | [`<stdlib.h>`](https://developer.apple.comhttps://man.freebsd.org/cgi/man.cgi?exit(3)), [`<sysexits.h>`](https://developer.apple.comhttps://man.freebsd.org/cgi/man.cgi?sysexits(3)) |
| OpenBSD | [`<stdlib.h>`](https://developer.apple.comhttps://man.openbsd.org/exit.3), [`<sysexits.h>`](https://developer.apple.comhttps://man.openbsd.org/sysexits.3) |
| Windows | [`<stdlib.h>`](https://developer.apple.comhttps://learn.microsoft.com/en-us/cpp/c-runtime-library/exit-success-exit-failure) |

On macOS, FreeBSD, OpenBSD, and Windows, the full exit code reported by the process is reported to the parent process. Linux and other POSIX-like systems may only reliably report the low unsigned 8 bits (0–255) of the exit code.

## Parameters

- `exitCode`: The exit code reported by the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/exitstatus/exitcode(_:))*