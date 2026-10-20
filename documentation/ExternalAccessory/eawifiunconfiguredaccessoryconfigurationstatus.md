# EAWiFiUnconfiguredAccessoryConfigurationStatus

**Framework**: External Accessory  
**Kind**: enum  
**Role**: Enumeration

Values that represent the state of the configuration process for an [`EAWiFiUnconfiguredAccessory`](./eawifiunconfiguredaccessory.md) object.

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

```c
enum EAWiFiUnconfiguredAccessoryConfigurationStatus : NSInteger;
```

## Topics

### Status Values
- [EAWiFiUnconfiguredAccessoryConfigurationStatus.success](./eawifiunconfiguredaccessoryconfigurationstatus/success.md)
  The configuration of the accessory succeeded.
- [EAWiFiUnconfiguredAccessoryConfigurationStatus.userCancelledConfiguration](./eawifiunconfiguredaccessoryconfigurationstatus/usercancelledconfiguration.md)
  The user cancelled the configuration process.
- [EAWiFiUnconfiguredAccessoryConfigurationStatus.failed](./eawifiunconfiguredaccessoryconfigurationstatus/failed.md)
  The configuration failed.
### Initializers
- [init?(rawValue: Int)](./eawifiunconfiguredaccessoryconfigurationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Updates About the Configuration Process
- [func accessoryBrowser(EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory: EAWiFiUnconfiguredAccessory, with: EAWiFiUnconfiguredAccessoryConfigurationStatus)](./eawifiunconfiguredaccessorybrowserdelegate/accessorybrowser%28_,didfinishconfiguringaccessory,with%29.md)
  Indicates that the browser has completed configuring the specified accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus)*