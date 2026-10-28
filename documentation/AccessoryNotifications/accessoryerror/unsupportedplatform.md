# AccessoryError.unsupportedPlatform

**Framework**: Accessory Notifications  
**Kind**: case  
**Role**: Case

An error that indicates the current platform doesn’t support notification forwarding.

**Availability**:
- iOS 26.5+

## Declaration

```swift
case unsupportedPlatform
```

## Discussion

This error can occur if you call [`requestForwarding(for:)`](../accessorynotificationcenter/requestforwarding%28for%29.md) on a platform other than iOS.

## See Also

### Platform and accessory errors
- [AccessoryError.unsupportedAccessory](./unsupportedaccessory.md)
  An error that indicates the system doesn’t support notification forwarding for the provided accessory.
- [AccessoryError.accessoryNotificationsUnavailable](./accessorynotificationsunavailable.md)
  An error that indicates accessory notifications aren’t available in the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror/unsupportedplatform)*