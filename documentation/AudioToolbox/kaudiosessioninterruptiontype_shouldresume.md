# kAudioSessionInterruptionType_ShouldResume

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

Indicates that the interruption that has just ended was one for which it is appropriate to immediately resume playback; for example, an incoming phone call was rejected by the user.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
var kAudioSessionInterruptionType_ShouldResume: Int { get }
```

```c
kAudioSessionInterruptionType_ShouldResume
```

## See Also

### Constants
- [var kAudioSessionInterruptionType_ShouldNotResume: Int](./kaudiosessioninterruptiontype_shouldnotresume.md)
  Indicates that the interruption that has just ended was one for which it is not appropriate to resume playback; for example, your app had been interrupted by iPod playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessioninterruptiontype_shouldresume)*