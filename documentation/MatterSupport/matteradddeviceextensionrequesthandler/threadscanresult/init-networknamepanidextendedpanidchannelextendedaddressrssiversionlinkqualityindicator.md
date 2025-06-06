# init(networkName:panID:extendedPANID:channel:extendedAddress:rssi:version:linkQualityIndicator:)

**Framework**: MatterSupport  
**Kind**: init

Create the extension request handler.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
init(networkName: String, panID: UInt16, extendedPANID: UInt64, channel: UInt16, extendedAddress: Data, rssi: Int8, version: UInt8, linkQualityIndicator: UInt8)
```

## Parameters

- `networkName`: The Thread network name.
- `extendedPANID`: The Thread network extended PAN identifier.
- `channel`: The Thread newtork radio channel.
- `extendedAddress`: The identifier of an active Thread network Border Agent.
- `rssi`: The observed RSSI of the network by the device.
- `version`: The version field, as specified by the Matter specification.
- `linkQualityIndicator`: A receive quality indicator, as specified by the Matter specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadscanresult/init(networkname:panid:extendedpanid:channel:extendedaddress:rssi:version:linkqualityindicator:))*