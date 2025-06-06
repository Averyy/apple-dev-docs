# NSHangOnTopLevelExceptionMask

**Framework**: Exception Handling  
**Kind**: var

The exception handler suspends execution when it detects an exception that would be handled by the top-level handler.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var NSHangOnTopLevelExceptionMask: Int { get }
```

## See Also

- [var NSHangOnUncaughtExceptionMask: Int](nshangonuncaughtexceptionmask.md)
  The exception handler suspends execution when it detects an uncaught exception (other than a system exception or runtime error).
- [var NSHangOnUncaughtSystemExceptionMask: Int](nshangonuncaughtsystemexceptionmask.md)
  The exception handler suspends execution when it detects an uncaught system exception.
- [var NSHangOnUncaughtRuntimeErrorMask: Int](nshangonuncaughtruntimeerrormask.md)
  The exception handler suspends execution when it detects an uncaught runtime error.
- [var NSHangOnOtherExceptionMask: Int](nshangonotherexceptionmask.md)
  The exception handler suspends execution when it detects an exception that would be handled by an object other than the top-level handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nshangontoplevelexceptionmask)*