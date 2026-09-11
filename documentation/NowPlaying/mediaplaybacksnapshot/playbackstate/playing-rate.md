# MediaPlaybackSnapshot.PlaybackState.playing(rate:)

**Framework**: Now Playing  
**Kind**: case

Content is currently playing.

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
case playing(rate: Float = 1.0)
```

#### Discussion

The associated `rate` reflects the actual speed at which content is advancing, including temporary changes like seeking (for example, `5.0` during fast-forward).


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediaplaybacksnapshot/playbackstate/playing(rate:))*