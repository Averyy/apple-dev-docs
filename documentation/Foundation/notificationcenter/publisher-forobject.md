# publisher(for:object:)

**Framework**: Foundation  
**Kind**: method

Returns a publisher that emits events when broadcasting notifications.

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
func publisher(for name: Notification.Name, object: AnyObject? = nil) -> NotificationCenter.Publisher
```

#### Return Value

A [`Publisher`](https://developer.apple.com/documentation/Combine/Publisher) that emits events when broadcasting notifications.

## Parameters

- `name`: The name of the notification to publish.
- `object`: The object posting the named notification. If  , the publisher emits elements for any object producing a notification with the given name.

## See Also

- [NotificationCenter.Publisher](notificationcenter/publisher.md)
  A publisher that emits elements when broadcasting notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/publisher(for:object:))*