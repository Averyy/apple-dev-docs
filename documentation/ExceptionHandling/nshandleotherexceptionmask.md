# NSHandleOtherExceptionMask

**Framework**: Exception Handling  
**Kind**: var

The exception handler handles exceptions caught by handlers lower than the top-level handler by converting them to [`NSException`](https://developer.apple.com/documentation/Foundation/NSException) objects containing a stack trace.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var NSHandleOtherExceptionMask: Int { get }
```

## See Also

- [var NSLogUncaughtExceptionMask: Int](nsloguncaughtexceptionmask.md)
  The exception handler logs uncaught exceptions.
- [var NSHandleUncaughtExceptionMask: Int](nshandleuncaughtexceptionmask.md)
  The exception handler handles uncaught exceptions by terminating the thread in which they occur.
- [var NSLogUncaughtSystemExceptionMask: Int](nsloguncaughtsystemexceptionmask.md)
  The exception handler logs uncaught system exceptions.
- [var NSHandleUncaughtSystemExceptionMask: Int](nshandleuncaughtsystemexceptionmask.md)
  The exception handler handles uncaught system exceptions by converting them to [`NSException`](https://developer.apple.com/documentation/Foundation/NSException) objects containing a stack trace.
- [var NSLogUncaughtRuntimeErrorMask: Int](nsloguncaughtruntimeerrormask.md)
  The exception handler logs uncaught runtime errors.
- [var NSHandleUncaughtRuntimeErrorMask: Int](nshandleuncaughtruntimeerrormask.md)
  The exception handler handles uncaught runtime errors by converting them to [`NSException`](https://developer.apple.com/documentation/Foundation/NSException) objects containing a stack trace.
- [var NSLogTopLevelExceptionMask: Int](nslogtoplevelexceptionmask.md)
  The exception handler logs exceptions that would be caught by the top-level handler.
- [var NSHandleTopLevelExceptionMask: Int](nshandletoplevelexceptionmask.md)
  The exception handler handles exceptions caught by the top-level handler by converting them to [`NSException`](https://developer.apple.com/documentation/Foundation/NSException) objects containing a stack trace.
- [var NSLogOtherExceptionMask: Int](nslogotherexceptionmask.md)
  The exception handler logs exceptions caught by handlers lower than the top-level handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nshandleotherexceptionmask)*