# AccessoryError.unsupportedAccessory

**Framework**: Accessory Notifications  
**Kind**: case  
**Role**: Case

An error that indicates the system doesn’t support notification forwarding for the provided accessory.

**Availability**:
- iOS 26.5+

## Declaration

```swift
case unsupportedAccessory
```

## Discussion

This error indicates that the argument specified in the [`requestForwarding(for:)`](../accessorynotificationcenter/requestforwarding%28for%29.md) call doesn’t support notification forwarding.

## See Also

### Platform and accessory errors
- [AccessoryError.unsupportedPlatform](./unsupportedplatform.md)
  An error that indicates the current platform doesn’t support notification forwarding.
- [AccessoryError.accessoryNotificationsUnavailable](./accessorynotificationsunavailable.md)
  An error that indicates accessory notifications aren’t available in the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror/unsupportedaccessory)*