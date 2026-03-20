# AccessoryNotificationCenter

**Framework**: Accessory Notifications  
**Kind**: class

A class that enables an app to request permission for notification forwarding.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class AccessoryNotificationCenter
```

#### Overview

Use this class from your accessory’s companion app to begin the notification forwarding lifecycle by calling [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md).

## Topics

### Creating a notification center
- [init()](accessorynotificationcenter/init.md)
  Initializes an accessory notifications center object.
### Requesting notification forwarding
- [func requestForwarding(for: ASAccessory) async throws -> ForwardingDecision](accessorynotificationcenter/requestforwarding(for:).md)
  Requests permission to forward notifications to the specified accessory.

## See Also

- [enum ForwardingDecision](forwardingdecision.md)
  Possible decisions in response to the notification forwarding permission prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter)*