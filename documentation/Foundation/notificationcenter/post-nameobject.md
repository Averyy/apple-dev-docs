# post(name:object:)

**Framework**: Foundation  
**Kind**: method

Creates a notification with a given name and sender and posts it to the notification center.

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
func post(name aName: NSNotification.Name, object anObject: Any?)
```

#### Discussion

This is a convenience method for calling [`post(name:object:userInfo:)`](notificationcenter/post(name:object:userinfo:).md) and passing `nil` to `aUserInfo`.

## Parameters

- `aName`: The name of the notification.
- `anObject`: The object posting the notification.

## See Also

- [func post(Notification)](notificationcenter/post(_:)-3x2st.md)
  Posts a given notification to the notification center.
- [func post(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](notificationcenter/post(name:object:userinfo:).md)
  Creates a notification with a given name, sender, and information and posts it to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(name:object:))*