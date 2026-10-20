# state

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

A state that represents the level of user interaction with the device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var state: DDDeviceState { get set }
```

```objc
@property (nonatomic, assign, readwrite) DDDeviceState state;
```

## See Also

### Setting the device state
- [var txtRecord: NWTXTRecord?](./txtrecord.md)
  A dictionary of metadata for the device that the extension communicates with over the local network.
- [var url: URL](./url.md)
  A resource locator for the simple service discovery protocol.
- [var supportsGrouping: Bool](./supportsgrouping.md)
  A Boolean value that indicates whether to group the device with others in the AirPlay UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/state)*