# AccessoryError

**Framework**: Accessory Notifications  
**Kind**: enum

Errors the Accessory Notifications framework can throw.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
enum AccessoryError
```

## Topics

### Platform and accessory errors
- [AccessoryError.accessoryNotificationsUnsupported](accessoryerror/accessorynotificationsunsupported.md)
  An error that indicates accessory notifications are not supported in the current configuration.
- [AccessoryError.unsupportedAccessory](accessoryerror/unsupportedaccessory.md)
  An error that indicates the system doesn’t support notification forwarding for the provided accessory.
- [AccessoryError.unsupportedPlatform](accessoryerror/unsupportedplatform.md)
  An error that indicates the current platform doesn’t support notification forwarding.
- [AccessoryError.unableToPresentSettings](accessoryerror/unabletopresentsettings.md)
  An error that indicates the system cannot present settings UI.
### Response errors
- [AccessoryError.coordinationTimeout](accessoryerror/coordinationtimeout.md)
  An error that indicates alert coordination timed out.
- [AccessoryError.invalidNotificationResponse](accessoryerror/invalidnotificationresponse.md)
  An error that indicates the system failed to handle a notification response.
- [AccessoryError.unableToGetUserResponse](accessoryerror/unabletogetuserresponse.md)
  An error that indicates the system is unable to handle a notification response.
### Communication errors
- [AccessoryError.nilXPCSession](accessoryerror/nilxpcsession.md)
  An error that indicates a failure in cross-process communication.
- [AccessoryError.invalidRequest](accessoryerror/invalidrequest.md)
  An error that indicates an invalid request.
- [AccessoryError.internalInconsistency](accessoryerror/internalinconsistency.md)
  An error that indicates an internal inconsistency.
### Custom errors
- [AccessoryError.customError(message:)](accessoryerror/customerror(message:).md)
  An error that provides a custom message.
- [init(customError: String)](accessoryerror/init(customerror:).md)
  Initializes an error with a custom message.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror)*