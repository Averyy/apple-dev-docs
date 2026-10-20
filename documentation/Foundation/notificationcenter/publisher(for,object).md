# publisher(for:object:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

A [`Publisher`](../../Combine/publisher.md) that emits events when broadcasting notifications.

## Parameters

- `name`: The name of the notification to publish.
- `object`: The object posting the named notification. If `nil`, the publisher emits elements for any object producing a notification with the given name.

## See Also

### Receiving notifications as a Combine publisher
- [NotificationCenter.Publisher](./publisher.md)
  A publisher that emits elements when broadcasting notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/publisher(for:object:))*