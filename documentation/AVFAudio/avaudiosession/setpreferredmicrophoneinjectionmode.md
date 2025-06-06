# setPreferredMicrophoneInjectionMode(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the preferred mode of injecting audio into another app’s input stream.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
func setPreferredMicrophoneInjectionMode(_ inValue: AVAudioSession.MicrophoneInjectionMode) throws
```

## Parameters

- `inValue`: The preferred microphone injection mode.

## See Also

- [var isMicrophoneInjectionAvailable: Bool](avaudiosession/ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](avaudiosession/preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](avaudiosession/microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredmicrophoneinjectionmode(_:))*