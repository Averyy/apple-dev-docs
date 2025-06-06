# kAudioSessionInterruptionType_ShouldNotResume

**Framework**: Audio Toolbox  
**Kind**: var

Indicates that the interruption that has just ended was one for which it is not appropriate to resume playback; for example, your app had been interrupted by iPod playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioSessionInterruptionType_ShouldNotResume: Int { get }
```

## See Also

- [var kAudioSessionInterruptionType_ShouldResume: Int](kaudiosessioninterruptiontype_shouldresume.md)
  Indicates that the interruption that has just ended was one for which it is appropriate to immediately resume playback; for example, an incoming phone call was rejected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninterruptiontype_shouldnotresume)*