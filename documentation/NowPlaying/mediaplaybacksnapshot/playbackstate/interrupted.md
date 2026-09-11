# MediaPlaybackSnapshot.PlaybackState.interrupted

**Framework**: Now Playing  
**Kind**: case

Playback was interrupted by the system.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case interrupted
```

#### Discussion

Use this state when playback is interrupted by system events such as a phone call or alarm. Your app is responsible for resuming playback when the interruption ends, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot/playbackstate/interrupted)*