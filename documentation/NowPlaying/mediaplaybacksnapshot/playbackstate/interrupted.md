# MediaPlaybackSnapshot.PlaybackState.interrupted

**Framework**: Now Playing  
**Kind**: case

Playback was interrupted by the system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case interrupted
```

#### Discussion

Use this state when playback is interrupted by system events such as a phone call or alarm. Your app is responsible for resuming playback when the interruption ends, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot/playbackstate/interrupted)*