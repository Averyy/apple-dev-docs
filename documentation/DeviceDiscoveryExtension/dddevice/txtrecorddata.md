# txtRecordData

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

A dictionary of metadata for the device that the extension communicates with over the local network.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite, nullable) NSData * txtRecordData;
```

## Discussion

Particularly, this dictionary provides the human-readable device name with its `"NAME"` key.

## See Also

### Setting the device state
- [var state: DDDeviceState](./state.md)
  A state that represents the level of user interaction with the device.
- [var url: URL](./url.md)
  A resource locator for the simple service discovery protocol.
- [var supportsGrouping: Bool](./supportsgrouping.md)
  A Boolean value that indicates whether to group the device with others in the AirPlay UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/txtrecorddata)*