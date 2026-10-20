# kAudioSessionSetActiveFlag_NotifyOthersOnDeactivation

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

Indicates that when your audio session deactivates, other audio sessions that had been interrupted by your session can return to their active state.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

> **Deprecated**: Deprecated in iOS 7.0.

## Declaration

```swift
var kAudioSessionSetActiveFlag_NotifyOthersOnDeactivation: Int { get }
```

```c
kAudioSessionSetActiveFlag_NotifyOthersOnDeactivation
```

#### Discussion

Used only when deactivating your audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiosessionsetactiveflag_notifyothersondeactivation)*