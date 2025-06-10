# DDDevice.MediaPlaybackState

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum

States that indicate the status of a device’s media playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
enum MediaPlaybackState
```

#### Overview

The device ([`DDDevice`](dddevice.md)) property [`mediaPlaybackState`](dddevice/mediaplaybackstate-swift.property.md) is of this type.

## Topics

### Distinguishing media playback states
- [DDDevice.MediaPlaybackState.noContent](dddevice/mediaplaybackstate-swift.enum/nocontent.md)
  A state that indicates when the device plays no content.
- [DDDevice.MediaPlaybackState.paused](dddevice/mediaplaybackstate-swift.enum/paused.md)
  A state that indicates when content playback for the device pauses.
- [DDDevice.MediaPlaybackState.playing](dddevice/mediaplaybackstate-swift.enum/playing.md)
  A state that indicates when the device plays media.
### Initializers
- [init?(rawValue: Int)](dddevice/mediaplaybackstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var mediaContentTitle: String?](dddevice/mediacontenttitle.md)
  A title for the current media that the device plays.
- [var mediaContentSubtitle: String?](dddevice/mediacontentsubtitle.md)
  A subtitle for the current media that the device plays.
- [var mediaPlaybackState: DDDevice.MediaPlaybackState](dddevice/mediaplaybackstate-swift.property.md)
  A playback status for the device’s current media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/mediaplaybackstate-swift.enum)*