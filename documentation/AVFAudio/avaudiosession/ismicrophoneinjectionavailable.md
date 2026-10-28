# isMicrophoneInjectionAvailable

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether microphone injection is available.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- visionOS 2.2+

## Declaration

```swift
var isMicrophoneInjectionAvailable: Bool { get }
```

```objc
@property (readonly) BOOL isMicrophoneInjectionAvailable;
```

## Discussion

Observe changes to the value of this property by registering for notifications of type [`microphoneInjectionCapabilitiesChangeNotification`](./microphoneinjectioncapabilitieschangenotification.md).

## See Also

### Enabling adding audio to calls
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](./preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](./setpreferredmicrophoneinjectionmode%28_%29.md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [AVAudioSession.MicrophoneInjectionMode](./microphoneinjectionmode.md)
  The modes of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](./microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/ismicrophoneinjectionavailable)*