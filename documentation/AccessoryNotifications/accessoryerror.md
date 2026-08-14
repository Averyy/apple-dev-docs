# AccessoryError

**Framework**: Accessory Notifications  
**Kind**: enum

Errors the Accessory Notifications framework can throw.

**Availability**:
- iOS 26.5+

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
- [AccessoryError.accessoryNotificationsUnavailable](accessoryerror/accessorynotificationsunavailable.md)
  An error that indicates accessory notifications aren’t available in the current configuration.
### Response errors
- [AccessoryError.invalidNotificationResponse](accessoryerror/invalidnotificationresponse.md)
  An error that indicates the system failed to handle a notification response.
- [AccessoryError.coordinationTimeout](accessoryerror/coordinationtimeout.md)
  An error that indicates alert coordination timed out.
### Communication errors
- [AccessoryError.internalInconsistency](accessoryerror/internalinconsistency.md)
  An error that indicates an internal inconsistency.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror)*