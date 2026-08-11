# disconnectedFromSystemAudio

**Framework**: AVFoundation  
**Kind**: property

Indicates whether the player is disconnected from system audio.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
var disconnectedFromSystemAudio: Bool { get }
```

#### Discussion

When NO (the default), the player is connected to system audio and coordinates with the application’s shared `AVAudioSession`. This implies that the player will activate the audio session when playback starts, render audio, and automatically reconfigure itself after events like route changes.

When YES, the player is disconnected from system audio and will not interact with the audio session. It will not activate the audio session when starting and it does not reconfigure after route changes. Specifically, this implies that such a player will not play audio until the property changes back to NO.

The value of this property can be changed dynamically during playback using setDisconnectedFromSystemAudio:completionHandler:.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/disconnectedfromsystemaudio)*