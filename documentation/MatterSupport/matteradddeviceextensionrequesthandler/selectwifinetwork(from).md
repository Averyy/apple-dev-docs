# selectWiFiNetwork(from:)

**Framework**: MatterSupport  
**Kind**: method  
**Role**: Instance Method

Provides the visible Wi-Fi networks to the Matter device.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
func selectWiFiNetwork(from wifiScanResults: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation
```

## Return Value

The Wi-Fi network to join, or [`defaultSystemNetwork`](./wifinetworkassociation/defaultsystemnetwork.md).

## Discussion

This completion handler informs the device which Wi-Fi network it needs to join. The Matter device can provide information about the visible Wi-Fi networks that it sees, in order to provide the ability to choose the correct network on which to put the device. This method is a way for the ecosystem to choose the correct network for the device to use.

The system may provide the selected Wi-Fi network in the completion handler. It must contain the credentials needed to associate to the selected network. The iOS device must be able to send the device IP traffic after it associates to the given network. Otherwise, if the return value is [`defaultSystemNetwork`](./wifinetworkassociation/defaultsystemnetwork.md), the system attempts to use the current network to which this device is associated.

iOS doesn’t store any credentials.

If the Matter device is already commissioned with a network, the selected network may do nothing.

## See Also

### Selecting the Wi-Fi network
- [MatterAddDeviceExtensionRequestHandler.WiFiScanResult](./wifiscanresult.md)
  A result of a Wi-Fi-scan operation performed on the device
- [MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](./wifinetworkassociation.md)
  The description of an association to a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/selectwifinetwork(from:))*