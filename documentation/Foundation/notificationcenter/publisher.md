# NotificationCenter.Publisher

**Framework**: Foundation  
**Kind**: struct

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

### Creating a Notification Publisher
- [init(center: NotificationCenter, name: Notification.Name, object: AnyObject?)](notificationcenter/publisher/init(center:name:object:).md)
  Creates a publisher that emits events when broadcasting notifications.
### Inspecting Notification Center Properties
- [let center: NotificationCenter](notificationcenter/publisher/center.md)
  The notification center this publisher uses as a source.
- [let name: Notification.Name](notificationcenter/publisher/name.md)
  The name of notifications published by this publisher.
- [let object: AnyObject?](notificationcenter/publisher/object.md)
  The object posting the named notfication.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](../Combine/Publisher.md)

## See Also

- [func publisher(for: Notification.Name, object: AnyObject?) -> NotificationCenter.Publisher](notificationcenter/publisher(for:object:).md)
  Returns a publisher that emits events when broadcasting notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/publisher)*