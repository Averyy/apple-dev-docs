# mediaPlaybackState

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

A playback status for the device’s current media.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Please use MediaDeviceExtension

## Declaration

```swift
var mediaPlaybackState: DDDevice.MediaPlaybackState { get set }
```

```objc
@property (nonatomic, assign, readwrite) DDDeviceMediaPlaybackState mediaPlaybackState;
```

## Discussion

Your app’s extension sets a value for this property to communicate to the system whether the device currently plays media. While the device plays, the system displays an equalizer animation next to the device in the picker UI.

## See Also

### Communicating device content and playback status
- [var mediaContentTitle: String?](./mediacontenttitle.md)
  A title for the current media that the device plays.
- [var mediaContentSubtitle: String?](./mediacontentsubtitle.md)
  A subtitle for the current media that the device plays.
- [DDDevice.MediaPlaybackState](./mediaplaybackstate-swift.enum.md)
  States that indicate the status of a device’s media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/mediaplaybackstate-swift.property)*