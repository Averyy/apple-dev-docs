# AccessoryNotificationCenter

**Framework**: Accessory Notifications  
**Kind**: class

A class that asks a person for permission to forward notifications.

**Availability**:
- iOS 26.5+

## Declaration

```swift
class AccessoryNotificationCenter
```

#### Overview

Use this class from your accessory’s companion app to begin the notification forwarding life cycle by calling [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md).

## Topics

### Creating a notification center
- [init()](accessorynotificationcenter/init.md)
  Initializes an accessory notifications center object.
### Requesting notification forwarding
- [func requestForwarding(for: ASAccessory) async throws -> ForwardingDecision](accessorynotificationcenter/requestforwarding(for:).md)
  Requests permission to forward notifications and Live Activities to the specified accessory.
### Checking forwarding status
- [func forwardingStatus(for: ASAccessory) async throws -> ForwardingDecision](accessorynotificationcenter/forwardingstatus(for:).md)
  Retrieves the current notification forwarding status for an accessory.
### Managing notification settings
- [func presentSettings(for: ASAccessory, scenePersistentIdentifier: String?) async throws -> ForwardingDecision](accessorynotificationcenter/presentsettings(for:scenepersistentidentifier:).md)
  Presents notification forwarding settings for an accessory.

## See Also

- [enum ForwardingDecision](forwardingdecision.md)
  Possible decisions in response to the notification forwarding permission prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter)*