# AVPlaybackUserInterfaceVolumeControllable

**Framework**: AVKit  
**Kind**: protocol

Provides volume and audio muting control for media content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
protocol AVPlaybackUserInterfaceVolumeControllable : AnyObject, Observable
```

## Topics

### Instance Properties
- [var hasAudio: Bool](avplaybackuserinterfacevolumecontrollable-4vgi1/hasaudio.md)
  Indicates whether the media contains audio tracks.
- [var isMuted: Bool](avplaybackuserinterfacevolumecontrollable-4vgi1/ismuted.md)
  Controls whether audio output is temporarily silenced.
- [var volume: Float](avplaybackuserinterfacevolumecontrollable-4vgi1/volume.md)
  The audio output volume as a normalized value between 0.0 and 1.0.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacevolumecontrollable-4vgi1)*