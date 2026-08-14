# EAWiFiUnconfiguredAccessoryConfigurationStatus

**Framework**: External Accessory  
**Kind**: enum

Values that represent the state of the configuration process for an [`EAWiFiUnconfiguredAccessory`](eawifiunconfiguredaccessory.md) object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum EAWiFiUnconfiguredAccessoryConfigurationStatus
```

## Topics

### Status Values
- [EAWiFiUnconfiguredAccessoryConfigurationStatus.success](eawifiunconfiguredaccessoryconfigurationstatus/success.md)
  The configuration of the accessory succeeded.
- [EAWiFiUnconfiguredAccessoryConfigurationStatus.userCancelledConfiguration](eawifiunconfiguredaccessoryconfigurationstatus/usercancelledconfiguration.md)
  The user cancelled the configuration process.
- [EAWiFiUnconfiguredAccessoryConfigurationStatus.failed](eawifiunconfiguredaccessoryconfigurationstatus/failed.md)
  The configuration failed.
### Initializers
- [init?(rawValue: Int)](eawifiunconfiguredaccessoryconfigurationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory: EAWiFiUnconfiguredAccessory, with: EAWiFiUnconfiguredAccessoryConfigurationStatus)](eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser(_:didfinishconfiguringaccessory:with:).md)
  Indicates that the browser has completed configuring the specified accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus)*