# txtRecord

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A dictionary of metadata for the device that the extension communicates with over the local network.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var txtRecord: NWTXTRecord? { get set }
```

#### Discussion

Particularly, this dictionary provides the human-readable device name with its `“NAME”` key.

## See Also

- [var state: DDDeviceState](dddevice/state.md)
  A state that represents the level of user interaction with the device.
- [var url: URL](dddevice/url.md)
  A resource locator for the simple service discovery protocol.
- [var supportsGrouping: Bool](dddevice/supportsgrouping.md)
  A Boolean value that indicates whether to group the device with others in the AirPlay UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/txtrecord)*