# NSGetUncaughtExceptionHandler()

**Framework**: Foundation  
**Kind**: func

Returns the top-level error handler.

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
func NSGetUncaughtExceptionHandler() -> ((NSException) -> Void)?
```

#### Return Value

A pointer to the top-level error-handling function where you can perform last-minute logging before the program terminates.

## See Also

- [func NSSetUncaughtExceptionHandler(((NSException) -> Void)?)](nssetuncaughtexceptionhandler(_:).md)
  Changes the top-level error handler.
- [func NSSetUncaughtExceptionHandler(((NSException) -> Void)?)](nssetuncaughtexceptionhandler(_:).md)
  Changes the top-level error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgetuncaughtexceptionhandler())*