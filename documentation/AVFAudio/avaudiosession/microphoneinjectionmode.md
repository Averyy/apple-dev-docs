# AVAudioSession.MicrophoneInjectionMode

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

The modes of injecting audio into another app’s input stream.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum MicrophoneInjectionMode
```

```c
enum AVAudioSessionMicrophoneInjectionMode : NSInteger;
```

## Overview

Apps can state their intent to mix synthesized speech into another app’s input stream. Accessibility apps can use this feature to implement augmentative and alternative communication systems that enable people with disabilities to communicate using synthesized speech.

> **Note**: When a person mutes audio input, the system also mutes microphone injection.

## Topics

### Creating an injection mode
- [init?(rawValue: Int)](./microphoneinjectionmode/init%28rawvalue%29.md)
### Choosing an injection mode
- [AVAudioSession.MicrophoneInjectionMode.none](./microphoneinjectionmode/none.md)
  A mode that indicates not to use spoken audio injection.
- [AVAudioSession.MicrophoneInjectionMode.spokenAudio](./microphoneinjectionmode/spokenaudio.md)
  A mode that indicates to inject spoken audio, like synthesized speech, along with microphone audio.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enabling adding audio to calls
- [var isMicrophoneInjectionAvailable: Bool](./ismicrophoneinjectionavailable.md)
  A Boolean value that indicates whether microphone injection is available.
- [var preferredMicrophoneInjectionMode: AVAudioSession.MicrophoneInjectionMode](./preferredmicrophoneinjectionmode.md)
  The preferred mode of injecting audio into another app’s input stream.
- [func setPreferredMicrophoneInjectionMode(AVAudioSession.MicrophoneInjectionMode) throws](./setpreferredmicrophoneinjectionmode%28_%29.md)
  Sets the preferred mode of injecting audio into another app’s input stream.
- [class let microphoneInjectionCapabilitiesChangeNotification: NSNotification.Name](./microphoneinjectioncapabilitieschangenotification.md)
  A notification the system posts when its capability to inject audio into an input stream changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/microphoneinjectionmode)*