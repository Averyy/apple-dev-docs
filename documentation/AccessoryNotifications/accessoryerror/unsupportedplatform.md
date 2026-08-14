# AccessoryError.unsupportedPlatform

**Framework**: Accessory Notifications  
**Kind**: case

An error that indicates the current platform doesn’t support notification forwarding.

**Availability**:
- iOS 26.5+

## Declaration

```swift
case unsupportedPlatform
```

#### Discussion

This error can occur if you call [`requestForwarding(for:)`](accessorynotificationcenter/requestforwarding(for:).md) on a platform other than iOS.

## See Also

- [AccessoryError.unsupportedAccessory](accessoryerror/unsupportedaccessory.md)
  An error that indicates the system doesn’t support notification forwarding for the provided accessory.
- [AccessoryError.accessoryNotificationsUnavailable](accessoryerror/accessorynotificationsunavailable.md)
  An error that indicates accessory notifications aren’t available in the current configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessoryerror/unsupportedplatform)*