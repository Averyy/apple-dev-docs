# extendedAddress

**Framework**: MatterSupport  
**Kind**: property

The identifier of an active Thread network Border Agent.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
var extendedAddress: Data
```

#### Discussion

This corresponds to the Border Agent ID in [`retrieveCredentials(forBorderAgent:completion:)`](https://developer.apple.com/documentation/ThreadNetwork/THClient/retrieveCredentials(forBorderAgent:completion:)).

## See Also

- [var channel: UInt16](matteradddeviceextensionrequesthandler/threadscanresult/channel.md)
  The Thread network radio channel.
- [var extendedPANID: UInt64](matteradddeviceextensionrequesthandler/threadscanresult/extendedpanid.md)
  The Thread network extended PAN identifier.
- [var linkQualityIndicator: UInt8](matteradddeviceextensionrequesthandler/threadscanresult/linkqualityindicator.md)
  A receive quality indicator, as specified by Matter specification.
- [var networkName: String](matteradddeviceextensionrequesthandler/threadscanresult/networkname.md)
  The Thread network name.
- [var panID: UInt16](matteradddeviceextensionrequesthandler/threadscanresult/panid.md)
  The Thread network PAN identifier.
- [var rssi: Int8](matteradddeviceextensionrequesthandler/threadscanresult/rssi.md)
  The observed RSSI of the network by the device.
- [var version: UInt8](matteradddeviceextensionrequesthandler/threadscanresult/version.md)
  The version field, as specified by the Matter specificaiton.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadscanresult/extendedaddress)*