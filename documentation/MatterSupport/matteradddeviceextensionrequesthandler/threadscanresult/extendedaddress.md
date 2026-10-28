# extendedAddress

**Framework**: MatterSupport  
**Kind**: property  
**Role**: Instance Property

The identifier of an active Thread network Border Agent.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
var extendedAddress: Data
```

## Discussion

This corresponds to the Border Agent ID in [`retrieveCredentials(forBorderAgent:completion:)`](../../../ThreadNetwork/thclient/retrievecredentials%28forborderagent,completion%29.md).

## See Also

### Getting result information
- [var channel: UInt16](./channel.md)
  The Thread network radio channel.
- [var extendedPANID: UInt64](./extendedpanid.md)
  The Thread network extended PAN identifier.
- [var linkQualityIndicator: UInt8](./linkqualityindicator.md)
  A receive quality indicator, as specified by Matter specification.
- [var networkName: String](./networkname.md)
  The Thread network name.
- [var panID: UInt16](./panid.md)
  The Thread network PAN identifier.
- [var rssi: Int8](./rssi.md)
  The observed RSSI of the network by the device.
- [var version: UInt8](./version.md)
  The version field, as specified by the Matter specification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadscanresult/extendedaddress)*