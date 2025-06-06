# NSSetUncaughtExceptionHandler(_:)

**Framework**: Foundation  
**Kind**: func

Changes the top-level error handler.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSSetUncaughtExceptionHandler(_: ((NSException) -> Void)?)
```

#### Discussion

Sets the top-level error-handling function where you can perform last-minute logging before the program terminates.

## See Also

- [func NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)?](nsgetuncaughtexceptionhandler().md)
  Returns the top-level error handler.
- [@MainActor func reportException(_ exception: NSException)](../AppKit/NSApplication/reportException(_:).md)
  Logs a given exception by calling `NSLog()`.
- [func NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)?](nsgetuncaughtexceptionhandler().md)
  Returns the top-level error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssetuncaughtexceptionhandler(_:))*