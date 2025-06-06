# init(ssid:rssi:security:band:)

**Framework**: MatterSupport  
**Kind**: init

Creates a new instance of the request handler.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
init(ssid: Data, rssi: Int8, security: MTRNetworkCommissioningWiFiSecurity, band: MTRNetworkCommissioningWiFiBand)
```

## Parameters

- `ssid`: The SSID of the Wi-Fi network.
- `rssi`: The device-observed RSSI of the network.
- `security`: The security method used to secure the Wi-Fi network.
- `band`: The band for the Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/wifiscanresult/init(ssid:rssi:security:band:))*