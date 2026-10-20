# MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

The description of an association to a Wi-Fi network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct WiFiNetworkAssociation
```

## Topics

### Getting network information
- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](./wifinetworkassociation/defaultsystemnetwork.md)
  The current Wi-Fi network of the iOS device.
- [static func network(ssid: Data, credentials: Data) -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](./wifinetworkassociation/network%28ssid,credentials%29.md)
  Maintains information about a specific Wi-Fi network.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selecting the Wi-Fi network
- [func selectWiFiNetwork(from: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](./selectwifinetwork%28from%29.md)
  Provides the visible Wi-Fi networks to the Matter device.
- [MatterAddDeviceExtensionRequestHandler.WiFiScanResult](./wifiscanresult.md)
  A result of a Wi-Fi-scan operation performed on the device


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/wifinetworkassociation)*