# NotificationCenter.Publisher

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A publisher that emits elements when broadcasting notifications.

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
struct Publisher
```

## Topics

### Declaring Publisher Topography
- [NotificationCenter.Publisher.Output](./publisher/output.md)
  The kind of values published by this publisher.
- [NotificationCenter.Publisher.Failure](./publisher/failure.md)
  The kind of errors this publisher might publish.
### Creating a Notification Publisher
- [init(center: NotificationCenter, name: Notification.Name, object: AnyObject?)](./publisher/init%28center,name,object%29.md)
  Creates a publisher that emits events when broadcasting notifications.
### Inspecting Notification Center Properties
- [let center: NotificationCenter](./publisher/center.md)
  The notification center this publisher uses as a source.
- [let name: Notification.Name](./publisher/name.md)
  The name of notifications published by this publisher.
- [let object: AnyObject?](./publisher/object.md)
  The object posting the named notfication.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../../Combine/publisher.md)

## See Also

### Receiving notifications as a Combine publisher
- [func publisher(for: Notification.Name, object: AnyObject?) -> NotificationCenter.Publisher](./publisher%28for,object%29.md)
  Returns a publisher that emits events when broadcasting notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/publisher)*