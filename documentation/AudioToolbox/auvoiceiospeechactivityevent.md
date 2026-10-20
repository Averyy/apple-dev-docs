# AUVoiceIOSpeechActivityEvent

**Framework**: Audio Toolbox  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the state of muted speech.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AUVoiceIOSpeechActivityEvent
```

```c
enum AUVoiceIOSpeechActivityEvent : UInt32;
```

## Topics

### Determining when muted speech starts and stops
- [AUVoiceIOSpeechActivityEvent.hasStarted](./auvoiceiospeechactivityevent/hasstarted.md)
  A state that indicates speech started.
- [AUVoiceIOSpeechActivityEvent.hasEnded](./auvoiceiospeechactivityevent/hasended.md)
  A state that indicates speech ended.
### Initializers
- [init?(rawValue: UInt32)](./auvoiceiospeechactivityevent/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Observing muted speech
- [var kAUVoiceIOProperty_MutedSpeechActivityEventListener: AudioUnitPropertyID](./kauvoiceioproperty_mutedspeechactivityeventlistener.md)
  A property to register a listener that the system calls when it detects speech while the user has the microphone muted.
- [typealias AUVoiceIOMutedSpeechActivityEventListener](./auvoiceiomutedspeechactivityeventlistener.md)
  A block that the system calls to indicate speech activity while the user has the microphone muted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auvoiceiospeechactivityevent)*