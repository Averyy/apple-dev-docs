# network(ssid:credentials:)

**Framework**: MatterSupport  
**Kind**: method

Maintains information about a specific Wi-Fi network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
static func network(ssid: Data, credentials: Data) -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation
```

#### Discussion

The credentials represent the passphrase that the system needs to associate to the SSID, if one is required. The security type of the Wi-Fi network determines the content of this field, its format, and its valid length.

## Parameters

- `ssid`: The SSID of the Wi-Fi network to associate to.
- `credentials`: The credentials that the sytems requires for associating to that network.

## See Also

- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/wifinetworkassociation/defaultsystemnetwork.md)
  The current Wi-Fi network of the iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/wifinetworkassociation/network(ssid:credentials:))*