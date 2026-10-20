# post(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Posts a given notification to the notification center.

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
func post(_ notification: Notification)
```

```objc
- (void) postNotification:(NSNotification *) notification;
```

## Parameters

- `notification`: The notification to post.

## See Also

### Posting notifications
- [func post(name: NSNotification.Name, object: Any?, userInfo: [AnyHashable : Any]?)](./post%28name,object,userinfo%29.md)
  Creates a notification with a given name, sender, and information and posts it to the notification center.
- [func post(name: NSNotification.Name, object: Any?)](./post%28name,object%29.md)
  Creates a notification with a given name and sender and posts it to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/post(_:)-3x2st)*