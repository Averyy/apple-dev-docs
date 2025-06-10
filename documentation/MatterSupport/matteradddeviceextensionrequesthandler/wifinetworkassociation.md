# MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation

**Framework**: MatterSupport  
**Kind**: struct

The description of an association to a Wi-Fi network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct WiFiNetworkAssociation
```

## Topics

### Getting network information
- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/wifinetworkassociation/defaultsystemnetwork.md)
  The current Wi-Fi network of the iOS device.
- [static func network(ssid: Data, credentials: Data) -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/wifinetworkassociation/network(ssid:credentials:).md)
  Maintains information about a specific Wi-Fi network.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func selectWiFiNetwork(from: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/selectwifinetwork(from:).md)
  Provides the visible Wi-Fi networks to the Matter device.
- [MatterAddDeviceExtensionRequestHandler.WiFiScanResult](matteradddeviceextensionrequesthandler/wifiscanresult.md)
  A result of a Wi-Fi-scan operation performed on the device


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/wifinetworkassociation)*