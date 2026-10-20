# preferredMicrophoneInjectionMode

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVAudioSessionMicrophoneInjectionMode preferredMicrophoneInjectionMode;
```

## See Also

### Enabling adding audio to calls
- [var isMicrophoneInjectionAvailable: Bool](./ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](./setpreferredmicrophoneinjectionmode%28_%29.md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](./microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](./microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredmicrophoneinjectionmode)*