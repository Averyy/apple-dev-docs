# notifyOthersOnDeactivation

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An option that indicates that the system should notify other apps that you’ve deactivated your app’s audio session.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var notifyOthersOnDeactivation: AVAudioSession.SetActiveOptions { get }
```

```c
AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation
```

#### Discussion

When passed in the `options` parameter of the [`setActive(_:options:)`](../setactive%28_,options%29.md) instance method, this option indicates that when your audio session deactivates, other audio sessions that had been interrupted by your session can return to their active state.

Only use this option when deactivating your audio session; that is, when you pass a value of [`false`](../../../Swift/false.md) to the [`setActive(_:options:)`](../setactive%28_,options%29.md) instance method.

## See Also

### Getting standard  options
- [var AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation: Int](../../avaudiosessionsetactiveflags_notifyothersondeactivation.md)
  A flag that indicates that when your audio session deactivates, any audio sessions that your audio session interrupted can reactivate themselves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactiveoptions/notifyothersondeactivation)*