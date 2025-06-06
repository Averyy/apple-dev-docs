# microphoneInjectionCapabilitiesChangeNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when its capability to inject audio into an input stream changes.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name
```

#### Discussion

Query the notification’s `userInfo` dictionary for [`AVAudioSessionMicrophoneInjectionIsAvailableKey`](avaudiosessionmicrophoneinjectionisavailablekey.md) to determine whether microphone injection is available.

## Topics

### User-information keys
- [let AVAudioSessionMicrophoneInjectionIsAvailableKey: String](avaudiosessionmicrophoneinjectionisavailablekey.md)
  A key to retrieve a Boolean value that indicates whether microphone injection is available.

## See Also

- [var isMicrophoneInjectionAvailable: Bool](avaudiosession/ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](avaudiosession/preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](avaudiosession/setpreferredmicrophoneinjectionmode(_:).md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](avaudiosession/microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/microphoneinjectioncapabilitieschangenotification)*