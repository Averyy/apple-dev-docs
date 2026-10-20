# AccessoryNotificationCenter

**Framework**: Accessory Notifications  
**Kind**: class  
**Role**: Class

A class that asks a person for permission to forward notifications.

**Availability**:
- iOS 26.5+

## Declaration

```swift
class AccessoryNotificationCenter
```

#### Overview

Use this class from your accessory’s companion app to begin the notification forwarding life cycle by calling [`requestForwarding(for:)`](./accessorynotificationcenter/requestforwarding%28for%29.md).

## Topics

### Creating a notification center
- [init()](./accessorynotificationcenter/init%28%29.md)
  Initializes an accessory notifications center object.
### Requesting notification forwarding
- [func requestForwarding(for: ASAccessory) async throws -> ForwardingDecision](./accessorynotificationcenter/requestforwarding%28for%29.md)
  Requests permission to forward notifications and Live Activities to the specified accessory.
### Checking forwarding status
- [func forwardingStatus(for: ASAccessory) async throws -> ForwardingDecision](./accessorynotificationcenter/forwardingstatus%28for%29.md)
  Retrieves the current notification forwarding status for an accessory.
### Managing notification settings
- [func presentSettings(for: ASAccessory, scenePersistentIdentifier: String?) async throws -> ForwardingDecision](./accessorynotificationcenter/presentsettings%28for,scenepersistentidentifier%29.md)
  Presents notification forwarding settings for an accessory.

## See Also

### Authorization
- [enum ForwardingDecision](./forwardingdecision.md)
  Possible decisions in response to the notification forwarding permission prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter)*