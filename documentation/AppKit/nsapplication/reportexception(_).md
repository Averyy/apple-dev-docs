# reportException(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Logs a given exception by calling `NSLog()`.

**Availability**:
- macOS

## Declaration

```swift
func reportException(_ exception: NSException)
```

```objc
- (void) reportException:(NSException *) exception;
```

#### Discussion

This method doesn’t raise `anException`. Use it inside of an exception handler to record that the exception occurred.

## Parameters

- `exception`: The exception whose contents you want to write to the log file.

## See Also

### Related Documentation
- [func NSSetUncaughtExceptionHandler(((NSException) -> Void)?)](../../Foundation/nssetuncaughtexceptionhandler%28_%29.md)
  Changes the top-level error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/reportexception(_:))*