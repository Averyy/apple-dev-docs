# mediaPlaybackState

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A playback status for the device’s current media.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var mediaPlaybackState: DDDevice.MediaPlaybackState { get set }
```

#### Discussion

Your app’s extension sets a value for this property to communicate to the system whether the device currently plays media. While the device plays, the system displays an equalizer animation next to the device in the picker UI.

## See Also

- [var mediaContentTitle: String?](dddevice/mediacontenttitle.md)
  A title for the current media that the device plays.
- [var mediaContentSubtitle: String?](dddevice/mediacontentsubtitle.md)
  A subtitle for the current media that the device plays.
- [DDDevice.MediaPlaybackState](dddevice/mediaplaybackstate-swift.enum.md)
  States that indicate the status of a device’s media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/mediaplaybackstate-swift.property)*