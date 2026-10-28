# mediaContentTitle

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

A title for the current media that the device plays.

**Availability**:
- iOS 16.0+ - Deprecated in 27.0
- iPadOS 16.0+ - Deprecated in 27.0
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Please use MediaDeviceExtension

## Declaration

```swift
var mediaContentTitle: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * mediaContentTitle;
```

## Discussion

Your app’s extension sets a value for this property to communicate to the system the particular media that the device currently plays. The system displays the information to the user in a Now Playing view in the picker UI.

Set this property to `nil` when [`mediaPlaybackState`](./mediaplaybackstate-swift.property.md) is [`DDDevice.MediaPlaybackState.noContent`](./mediaplaybackstate-swift.enum/nocontent.md).

## See Also

### Communicating device content and playback status
- [var mediaContentSubtitle: String?](./mediacontentsubtitle.md)
  A subtitle for the current media that the device plays.
- [var mediaPlaybackState: DDDevice.MediaPlaybackState](./mediaplaybackstate-swift.property.md)
  A playback status for the device’s current media.
- [DDDevice.MediaPlaybackState](./mediaplaybackstate-swift.enum.md)
  States that indicate the status of a device’s media playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/mediacontenttitle)*