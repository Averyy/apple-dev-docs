# beginSeekingBackward()

**Framework**: MusicKit  
**Kind**: method

Begins seeking backward through the music content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 14.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func beginSeekingBackward()
```

#### Discussion

Use this method to move the current playback position backward in time at an accelerated rate. Seeking begins when you call this method, and continues until you call the [`endSeeking()`](musicplayer/endseeking().md) method.

If the player is streaming the underlying content, this method has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicplayer/beginseekingbackward())*