# AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A flag that indicates that when your audio session deactivates, any audio sessions that your audio session interrupted can reactivate themselves.

**Availability**:
- iOS 4.0+ - Deprecated in 6.0 (renamed: AVAudioSessionSetActiveOptions)
- iPadOS 4.0+ - Deprecated in 6.0 (renamed: AVAudioSessionSetActiveOptions)
- Mac Catalyst 4.0+ - Deprecated in 6.0 (renamed: AVAudioSessionSetActiveOptions)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: AVAudioSessionSetActiveOptions)

> **Deprecated**: Use the constants in [`AVAudioSession.SetActiveOptions`](./avaudiosession/setactiveoptions.md) instead.

## Declaration

```swift
var AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation: Int { get }
```

```c
AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation
```

## Discussion

This flag works when passed in the `flags` parameter of the [`setActive(_:withFlags:)`](./avaudiosession/setactive%28_,withflags%29.md) instance method. You use this flag only when deactivating your audio session.

## See Also

### Getting standard  options
- [static var notifyOthersOnDeactivation: AVAudioSession.SetActiveOptions](./avaudiosession/setactiveoptions/notifyothersondeactivation.md)
  An option that indicates that the system should notify other apps that you’ve deactivated your app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionsetactiveflags_notifyothersondeactivation)*