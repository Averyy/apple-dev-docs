# AccessoryNotification.Identifier

**Framework**: Accessory Notifications  
**Kind**: struct

A structure that uniquely identifies a notification.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
struct Identifier
```

#### Overview

A notification’s [`identifier`](accessorynotification/identifier-swift.property.md) property is of this type.

## Topics

### Creating an identifier
- [init(notificationIdentifier: String, sourceIdentifier: String)](accessorynotification/identifier-swift.struct/init(notificationidentifier:sourceidentifier:).md)
### Accessing identifier components
- [let notificationIdentifier: String](accessorynotification/identifier-swift.struct/notificationidentifier.md)
  An identifier that the source app sets for the notification.
- [let sourceIdentifier: String](accessorynotification/identifier-swift.struct/sourceidentifier.md)
  The source app’s bundle identifier.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let identifier: AccessoryNotification.Identifier](accessorynotification/identifier-swift.property.md)
  A structure that uniquely identifies the notification.
- [let threadIdentifier: String?](accessorynotification/threadidentifier.md)
  An identifier that groups notifications that belong to the same thread.
- [let sourceName: String](accessorynotification/sourcename.md)
  A display name for the bundle that sent the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/identifier-swift.struct)*