# init(center:name:object:)

**Framework**: Foundation  
**Kind**: init

Creates a publisher that emits events when broadcasting notifications.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(center: NotificationCenter, name: Notification.Name, object: AnyObject? = nil)
```

## Parameters

- `center`: The notification center to publish notifications for.
- `name`: The name of the notification to publish.
- `object`: The object posting the named notfication. If  , the publisher emits elements for any object producing a notification with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/publisher/init(center:name:object:))*