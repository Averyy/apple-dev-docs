# microphoneInjectionCapabilitiesChangeNotification

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

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

```c
extern NSNotificationName const AVAudioSessionMicrophoneInjectionCapabilitiesChangeNotification;
```

#### Discussion

Query the notification’s `userInfo` dictionary for [`AVAudioSessionMicrophoneInjectionIsAvailableKey`](../avaudiosessionmicrophoneinjectionisavailablekey.md) to determine whether microphone injection is available.

## Topics

### User-information keys
- [let AVAudioSessionMicrophoneInjectionIsAvailableKey: String](../avaudiosessionmicrophoneinjectionisavailablekey.md)
  A key to retrieve a Boolean value that indicates whether microphone injection is available.

## See Also

### Enabling adding audio to calls
- [var isMicrophoneInjectionAvailable: Bool](./ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](./preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](./setpreferredmicrophoneinjectionmode%28_%29.md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](./microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/microphoneinjectioncapabilitieschangenotification)*