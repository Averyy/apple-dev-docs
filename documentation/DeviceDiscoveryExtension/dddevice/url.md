# url

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A resource locator for the simple service discovery protocol.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var url: URL { get set }
```

#### Discussion

Set this property to indicate communication with a device over the simple service discovery protocol (SSDP). The value needs to:

- Resolve to a valid hostname.
- Include no query parameters.
- Be of a size no greater than 100 bytes.

## See Also

- [var state: DDDeviceState](dddevice/state.md)
  A state that represents the level of user interaction with the device.
- [var txtRecord: NWTXTRecord?](dddevice/txtrecord.md)
  A dictionary of metadata for the device that the extension communicates with over the local network.
- [var supportsGrouping: Bool](dddevice/supportsgrouping.md)
  A Boolean value that indicates whether to group the device with others in the AirPlay UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/url)*