# MatterAddDeviceExtensionRequestHandler.WiFiScanResult

**Framework**: MatterSupport  
**Kind**: struct

A result of a Wi-Fi-scan operation performed on the device

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct WiFiScanResult
```

#### Overview

Use an instances to create a `WiFiNetworkAssociation` as a possible Wi-Fi network for the device to join.

## Topics

### Creating the result
- [init(ssid: Data, rssi: Int8, security: MTRNetworkCommissioningWiFiSecurity, band: MTRNetworkCommissioningWiFiBand)](matteradddeviceextensionrequesthandler/wifiscanresult/init(ssid:rssi:security:band:).md)
  Creates a new instance of the request handler.
### Getting result information
- [var band: MTRNetworkCommissioningWiFiBand](matteradddeviceextensionrequesthandler/wifiscanresult/band.md)
  The band for the Wi-Fi network.
- [var rssi: Int8](matteradddeviceextensionrequesthandler/wifiscanresult/rssi.md)
  The device-observed RSSI of the network.
- [var security: MTRNetworkCommissioningWiFiSecurity](matteradddeviceextensionrequesthandler/wifiscanresult/security.md)
  The security method used to secure the Wi-Fi network.
- [var ssid: Data](matteradddeviceextensionrequesthandler/wifiscanresult/ssid.md)
  The SSID of the Wi-Fi network.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func selectWiFiNetwork(from: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/selectwifinetwork(from:).md)
  Provides the visible Wi-Fi networks to the Matter device.
- [MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/wifinetworkassociation.md)
  The description of an association to a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/wifiscanresult)*