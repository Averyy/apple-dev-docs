# post(name:object:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) postNotificationName:(NSNotificationName) aName object:(id) anObject;
```

#### Discussion

This is a convenience method for calling [`post(name:object:userInfo:)`](./post%28name,object,userinfo%29.md) and passing `nil` to `aUserInfo`.

## Parameters

- `aName`: The name of the notification.
- `anObject`: The object posting the notification.

## See Also

### Posting notifications
- [func post(Notification)](./post%28_%29-3x2st.md)
  Posts a given notification to the notification center.
- [func post(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./post%28name,object,userinfo%29.md)
  Creates a notification with a given name, sender, and information and posts it to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(name:object:))*