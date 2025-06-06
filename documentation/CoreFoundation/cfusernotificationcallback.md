# CFUserNotificationCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when an asynchronous user notification dialog is dismissed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFUserNotificationCallBack = (CFUserNotification?, CFOptionFlags) -> Void
```

## Parameters

- `userNotification`: The user notification that was dismissed.
- `responseFlags`: On return, contains flags identifying how the notification was dismissed, the state of any checkboxes, and the selected item of the pop-up menu. See   for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationcallback)*