# NSHangOnUncaughtExceptionMask

**Framework**: Exception Handling  
**Kind**: var

The exception handler suspends execution when it detects an uncaught exception (other than a system exception or runtime error).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var NSHangOnUncaughtExceptionMask: Int { get }
```

## See Also

- [var NSHangOnUncaughtSystemExceptionMask: Int](nshangonuncaughtsystemexceptionmask.md)
  The exception handler suspends execution when it detects an uncaught system exception.
- [var NSHangOnUncaughtRuntimeErrorMask: Int](nshangonuncaughtruntimeerrormask.md)
  The exception handler suspends execution when it detects an uncaught runtime error.
- [var NSHangOnTopLevelExceptionMask: Int](nshangontoplevelexceptionmask.md)
  The exception handler suspends execution when it detects an exception that would be handled by the top-level handler.
- [var NSHangOnOtherExceptionMask: Int](nshangonotherexceptionmask.md)
  The exception handler suspends execution when it detects an exception that would be handled by an object other than the top-level handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nshangonuncaughtexceptionmask)*