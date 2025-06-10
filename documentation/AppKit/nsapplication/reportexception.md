# reportException(_:)

**Framework**: AppKit  
**Kind**: method

Logs a given exception by calling `NSLog()`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reportException(_ exception: NSException)
```

#### Discussion

This method doesn’t raise `anException`. Use it inside of an exception handler to record that the exception occurred.

## Parameters

- `exception`: The exception whose contents you want to write to the log file.

## See Also

- [func NSSetUncaughtExceptionHandler(_: ((NSException) -> Void)?)](../Foundation/NSSetUncaughtExceptionHandler(_:).md)
  Changes the top-level error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/reportexception(_:))*