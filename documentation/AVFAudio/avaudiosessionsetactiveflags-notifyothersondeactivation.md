# AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation

**Framework**: AVFAudio  
**Kind**: var

A flag that indicates that when your audio session deactivates, any audio sessions that your audio session interrupted can reactivate themselves.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation: Int { get }
```

#### Discussion

This flag works when passed in the `flags` parameter of the [`setActive(_:withFlags:)`](avaudiosession/setactive(_:withflags:).md) instance method. You use this flag only when deactivating your audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionsetactiveflags_notifyothersondeactivation)*