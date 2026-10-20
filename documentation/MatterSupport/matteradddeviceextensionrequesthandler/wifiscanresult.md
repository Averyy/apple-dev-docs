# MatterAddDeviceExtensionRequestHandler.WiFiScanResult

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

A result of a Wi-Fi-scan operation performed on the device

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct WiFiScanResult
```

#### Overview

Use an instances to create a `WiFiNetworkAssociation` as a possible Wi-Fi network for the device to join.

## Topics

### Creating the result
- [init(ssid: Data, rssi: Int8, security: MTRNetworkCommissioningWiFiSecurity, band: MTRNetworkCommissioningWiFiBand)](./wifiscanresult/init%28ssid,rssi,security,band%29.md)
  Creates a new instance of the request handler.
### Getting result information
- [var band: MTRNetworkCommissioningWiFiBand](./wifiscanresult/band.md)
  The band for the Wi-Fi network.
- [var rssi: Int8](./wifiscanresult/rssi.md)
  The device-observed RSSI of the network.
- [var security: MTRNetworkCommissioningWiFiSecurity](./wifiscanresult/security.md)
  The security method used to secure the Wi-Fi network.
- [var ssid: Data](./wifiscanresult/ssid.md)
  The SSID of the Wi-Fi network.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selecting the Wi-Fi network
- [func selectWiFiNetwork(from: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](./selectwifinetwork%28from%29.md)
  Provides the visible Wi-Fi networks to the Matter device.
- [MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](./wifinetworkassociation.md)
  The description of an association to a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/wifiscanresult)*