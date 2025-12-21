# NSStackTraceKey

**Framework**: Exception Handling  
**Kind**: var

The key for fetching the stack trace (an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object) in the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSException/userInfo-swift.property) dictionary of the [`NSException`](https://developer.apple.com/documentation/Foundation/NSException) object passed into one of the delegate methods described in [`NSExceptionHandlerDelegate`](nsexceptionhandlerdelegate#Logging-and-handling-exceptions.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let NSStackTraceKey: String
```

## See Also

- [let NSUncaughtRuntimeErrorException: String](nsuncaughtruntimeerrorexception.md)
  Identifies an Objective-C runtime error.
- [let NSUncaughtSystemExceptionException: String](nsuncaughtsystemexceptionexception.md)
  Identifies an uncaught system exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsstacktracekey)*