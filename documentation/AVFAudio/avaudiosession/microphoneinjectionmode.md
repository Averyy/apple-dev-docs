# AVAudioSession.MicrophoneInjectionMode

**Framework**: AVFAudio  
**Kind**: enum

The modes of injecting audio into another app’s input stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum MicrophoneInjectionMode
```

#### Overview

Apps can state their intent to mix synthesized speech into another app’s input stream. Accessibility apps can use this feature to implement augmentative and alternative communication systems that enable people with disabilities to communicate using synthesized speech.

> **Note**: When a person mutes audio input, the system also mutes microphone injection.

## Topics

### Microphone injection modes
- [AVAudioSession.MicrophoneInjectionMode.none](avaudiosession/microphoneinjectionmode/none.md)
  A mode that indicates not to use spoken audio injection.
- [AVAudioSession.MicrophoneInjectionMode.spokenAudio](avaudiosession/microphoneinjectionmode/spokenaudio.md)
  A mode that indicates to inject spoken audio, like synthesized speech, along with microphone audio.
### Initializers
- [init?(rawValue: Int)](avaudiosession/microphoneinjectionmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isMicrophoneInjectionAvailable: Bool](avaudiosession/ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](avaudiosession/preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](avaudiosession/setpreferredmicrophoneinjectionmode(_:).md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/microphoneinjectionmode)*