# post(name:object:userInfo:)

**Framework**: Foundation  
**Kind**: method

Creates a notification with a given name, sender, and information and posts it to the notification center.

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
func post(name aName: NSNotification.Name, object anObject: Any?, userInfo aUserInfo: [AnyHashable : Any]? = nil)
```

## Parameters

- `aName`: The name of the notification.
- `anObject`: The object posting the notification.
- `aUserInfo`: A user info dictionary with optional information about the notification.

## See Also

- [func post(Notification)](notificationcenter/post(_:).md)
  Posts a given notification to the notification center.
- [func post(name: NSNotification.Name, object: Any?)](notificationcenter/post(name:object:).md)
  Creates a notification with a given name and sender and posts it to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(name:object:userinfo:))*