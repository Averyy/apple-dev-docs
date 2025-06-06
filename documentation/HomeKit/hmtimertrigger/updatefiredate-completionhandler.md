# updateFireDate(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the next fire date for the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func updateFireDate(_ fireDate: Date) async throws
```

## Parameters

- `fireDate`: The new fire date.
- `completion`: The block executed after the request is processed.

## See Also

- [var fireDate: Date](hmtimertrigger/firedate.md)
  The time at which the trigger will next fire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtimertrigger/updatefiredate(_:completionhandler:))*