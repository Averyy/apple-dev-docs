# mediaContentSubtitle

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A subtitle for the current media that the device plays.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var mediaContentSubtitle: String? { get set }
```

#### Discussion

Your app’s extension sets a value for this property to communicate to the system the particular media that the device currently plays. The system displays the information to the user in a Now Playing view in the picker UI.

Set this property to `nil` when [`mediaPlaybackState`](dddevice/mediaplaybackstate-swift.property.md) is [`DDDevice.MediaPlaybackState.noContent`](dddevice/mediaplaybackstate-swift.enum/nocontent.md).

## See Also

- [var mediaContentTitle: String?](dddevice/mediacontenttitle.md)
  A title for the current media that the device plays.
- [var mediaPlaybackState: DDDevice.MediaPlaybackState](dddevice/mediaplaybackstate-swift.property.md)
  A playback status for the device’s current media.
- [DDDevice.MediaPlaybackState](dddevice/mediaplaybackstate-swift.enum.md)
  States that indicate the status of a device’s media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/mediacontentsubtitle)*