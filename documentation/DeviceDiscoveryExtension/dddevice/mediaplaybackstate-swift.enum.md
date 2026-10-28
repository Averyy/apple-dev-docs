# DDDevice.MediaPlaybackState

**Framework**: DeviceDiscoveryExtension  
**Kind**: enum  
**Role**: Enumeration

States that indicate the status of a device’s media playback.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
enum MediaPlaybackState
```

```c
enum DDDeviceMediaPlaybackState : NSInteger;
```

## Overview

The device ([`DDDevice`](../dddevice.md)) property [`mediaPlaybackState`](./mediaplaybackstate-swift.property.md) is of this type.

## Topics

### Distinguishing media playback states
- [DDDevice.MediaPlaybackState.noContent](./mediaplaybackstate-swift.enum/nocontent.md)
  A state that indicates when the device plays no content.
- [DDDevice.MediaPlaybackState.paused](./mediaplaybackstate-swift.enum/paused.md)
  A state that indicates when content playback for the device pauses.
- [DDDevice.MediaPlaybackState.playing](./mediaplaybackstate-swift.enum/playing.md)
  A state that indicates when the device plays media.
### Initializers
- [init?(rawValue: Int)](./mediaplaybackstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Communicating device content and playback status
- [var mediaContentTitle: String?](./mediacontenttitle.md)
  A title for the current media that the device plays.
- [var mediaContentSubtitle: String?](./mediacontentsubtitle.md)
  A subtitle for the current media that the device plays.
- [var mediaPlaybackState: DDDevice.MediaPlaybackState](./mediaplaybackstate-swift.property.md)
  A playback status for the device’s current media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/mediaplaybackstate-swift.enum)*