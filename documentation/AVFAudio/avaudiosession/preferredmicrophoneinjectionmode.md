# preferredMicrophoneInjectionMode

**Framework**: AVFAudio  
**Kind**: property

The preferred mode of injecting audio into another app’s input stream.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode { get }
```

## See Also

- [var isMicrophoneInjectionAvailable: Bool](avaudiosession/ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](avaudiosession/setpreferredmicrophoneinjectionmode(_:).md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](avaudiosession/microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredmicrophoneinjectionmode)*