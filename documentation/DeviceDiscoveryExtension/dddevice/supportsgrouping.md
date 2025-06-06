# supportsGrouping

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A Boolean value that indicates whether to group the device with others in the AirPlay UI.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var supportsGrouping: Bool { get set }
```

#### Discussion

This property provides a convenient way to send the same media stream to multiple devices and list them as a group in the AirPlay UI ([`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView)). For example, a set of speakers arranged around the room can implement stereo playback by each playing different audio channels from an audio stream.

When someone selects a media receiver in the AirPlay menu, the system checks if it supports grouping. If so, the AirPlay UI displays a checkbox next to any other media receivers that also support grouping and implement the same protocol ([`DDDevice.Protocol`](dddevice/protocol-swift.enum.md)).

If a person selects multiple devices in the menu, the selected devices reorder next to each other in the list.

> **Note**:  Implement [`didReceiveEvent(_:)`](dddiscoveryextension/didreceiveevent(_:).md) in the [`DDDiscoveryExtension`](dddiscoveryextension.md) to detect when a person changes the device grouping using the AirPlay UI.

 Implement [`didReceiveEvent(_:)`](dddiscoveryextension/didreceiveevent(_:).md) in the [`DDDiscoveryExtension`](dddiscoveryextension.md) to detect when a person changes the device grouping using the AirPlay UI.

## See Also

- [var state: DDDeviceState](dddevice/state.md)
  A state that represents the level of user interaction with the device.
- [var txtRecord: NWTXTRecord?](dddevice/txtrecord.md)
  A dictionary of metadata for the device that the extension communicates with over the local network.
- [var url: URL](dddevice/url.md)
  A resource locator for the simple service discovery protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/supportsgrouping)*