# AVInterfaceVolumeControllable

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
protocol AVInterfaceVolumeControllable : Observable
```

## Topics

### Controlling volume
- [var volume: Float](avinterfacevolumecontrollable-5sjm1/volume.md)
  The audio output level as a normalized value between 0.0 and 1.0.
- [var isMuted: Bool](avinterfacevolumecontrollable-5sjm1/ismuted.md)
  Controls whether audio output is temporarily silenced.
- [var hasAudio: Bool](avinterfacevolumecontrollable-5sjm1/hasaudio.md)
  Indicates whether the media contains audio tracks.

## Relationships

### Inherits From
- [Observable](../Observation/Observable.md)
### Inherited By
- [AVInterfaceControllable](avinterfacecontrollable-3xs3i.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacevolumecontrollable-5sjm1)*