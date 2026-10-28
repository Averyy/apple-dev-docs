# NSGetUncaughtExceptionHandler()

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern void (*)(NSException *)NSGetUncaughtExceptionHandler();
```

## Return Value

A pointer to the top-level error-handling function where you can perform last-minute logging before the program terminates.

## See Also

### Related Documentation
- [func NSSetUncaughtExceptionHandler(((NSException) -> Void)?)](./nssetuncaughtexceptionhandler%28_%29.md)
  Changes the top-level error handler.
### Functions
- [func NSSetUncaughtExceptionHandler(((NSException) -> Void)?)](./nssetuncaughtexceptionhandler%28_%29.md)
  Changes the top-level error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsgetuncaughtexceptionhandler())*