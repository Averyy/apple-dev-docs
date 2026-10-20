# kAudioSessionBeginInterruption

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

Your app’s audio session has just been interrupted, such as by a phone call.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
var kAudioSessionBeginInterruption: Int { get }
```

```c
kAudioSessionBeginInterruption
```

## See Also

### Constants
- [var kAudioSessionEndInterruption: Int](./kaudiosessionendinterruption.md)
  The interruption to your app’s audio session has just ended. In the case where a user confirms the interruption, such as answering a phone call, your app will not receive this constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionbegininterruption)*