# AccessoryError

**Framework**: Accessory Notifications  
**Kind**: enum

Errors the Accessory Notifications framework can throw.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
enum AccessoryError
```

## Topics

### Platform and accessory errors
- [AccessoryError.unsupportedAccessory](accessoryerror/unsupportedaccessory.md)
  An error that indicates the system doesn’t support notification forwarding for the provided accessory.
- [AccessoryError.unsupportedPlatform](accessoryerror/unsupportedplatform.md)
  An error that indicates the current platform doesn’t support notification forwarding.
### Response errors
- [AccessoryError.coordinationTimeout](accessoryerror/coordinationtimeout.md)
  An error that indicates alert coordination timed out.
- [AccessoryError.invalidNotificationResponse](accessoryerror/invalidnotificationresponse.md)
  An error that indicates the system failed to handle a notification response.
### Communication errors
- [AccessoryError.internalInconsistency](accessoryerror/internalinconsistency.md)
  An error that indicates an internal inconsistency.
### Enumeration Cases
- [AccessoryError.accessoryNotificationsUnavailable](accessoryerror/accessorynotificationsunavailable.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror)*