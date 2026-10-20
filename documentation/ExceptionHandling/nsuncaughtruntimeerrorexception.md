# NSUncaughtRuntimeErrorException

**Framework**: Exception Handling  
**Kind**: var  
**Role**: Global Variable

Identifies an Objective-C runtime error.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let NSUncaughtRuntimeErrorException: String
```

```c
extern NSString * NSUncaughtRuntimeErrorException;
```

## See Also

### Constants
- [let NSStackTraceKey: String](./nsstacktracekey.md)
  The key for fetching the stack trace (an [`NSString`](../Foundation/nsstring.md) object) in the [`userInfo`](../Foundation/nsexception/userinfo-swift.property.md) dictionary of the [`NSException`](../Foundation/nsexception.md) object passed into one of the delegate methods described in [NSExceptionHandlerDelegate](./nsexceptionhandlerdelegate.md).
- [let NSUncaughtSystemExceptionException: String](./nsuncaughtsystemexceptionexception.md)
  Identifies an uncaught system exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exceptionhandling/nsuncaughtruntimeerrorexception)*