# post(name:object:userInfo:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) postNotificationName:(NSNotificationName) aName object:(id) anObject userInfo:(NSDictionary *) aUserInfo;
```

## Parameters

- `aName`: The name of the notification.
- `anObject`: The object posting the notification.
- `aUserInfo`: A user info dictionary with optional information about the notification.

## See Also

### Posting notifications
- [func post(Notification)](./post%28_%29-3x2st.md)
  Posts a given notification to the notification center.
- [func post(name: NSNotification.Name, object: Any?)](./post%28name,object%29.md)
  Creates a notification with a given name and sender and posts it to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(name:object:userinfo:))*