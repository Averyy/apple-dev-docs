# CFUserNotificationCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Callback invoked when an asynchronous user notification dialog is dismissed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFUserNotificationCallBack = (CFUserNotification?, CFOptionFlags) -> Void
```

```c
typedef void (*)(struct __CFUserNotification *, unsigned long) CFUserNotificationCallBack;
```

## Parameters

- `userNotification`: The user notification that was dismissed.
- `responseFlags`: On return, contains flags identifying how the notification was dismissed, the state of any checkboxes, and the selected item of the pop-up menu. See [`CFUserNotificationReceiveResponse(_:_:_:)`](./cfusernotificationreceiveresponse%28_,_,_%29.md) for details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfusernotificationcallback)*