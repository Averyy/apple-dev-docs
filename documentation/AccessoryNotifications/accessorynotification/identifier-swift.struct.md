# AccessoryNotification.Identifier

**Framework**: Accessory Notifications  
**Kind**: struct  
**Role**: Structure

A structure that uniquely identifies a notification.

**Availability**:
- iOS 26.5+

## Declaration

```swift
struct Identifier
```

#### Overview

A notification’s [`identifier`](./identifier-swift.property.md) property is of this type.

## Topics

### Creating an identifier
- [init(notificationIdentifier: String, sourceIdentifier: String)](./identifier-swift.struct/init%28notificationidentifier,sourceidentifier%29.md)
  Initializes a notification identifier from its components.
### Accessing identifier components
- [let notificationIdentifier: String](./identifier-swift.struct/notificationidentifier.md)
  An identifier that the source app sets for the notification.
- [let sourceIdentifier: String](./identifier-swift.struct/sourceidentifier.md)
  The source app’s bundle identifier.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying and grouping notifications
- [let identifier: AccessoryNotification.Identifier](./identifier-swift.property.md)
  A structure that uniquely identifies the notification.
- [let threadIdentifier: String?](./threadidentifier.md)
  An identifier that groups notifications that belong to the same thread.
- [let sourceName: String](./sourcename.md)
  A display name for the bundle that sent the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotification/identifier-swift.struct)*