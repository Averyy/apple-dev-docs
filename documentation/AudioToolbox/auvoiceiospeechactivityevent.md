# AUVoiceIOSpeechActivityEvent

**Framework**: Audio Toolbox  
**Kind**: enum

Constants that indicate the state of muted speech.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AUVoiceIOSpeechActivityEvent
```

## Topics

### Determining when muted speech starts and stops
- [AUVoiceIOSpeechActivityEvent.hasStarted](auvoiceiospeechactivityevent/hasstarted.md)
  A state that indicates speech started.
- [AUVoiceIOSpeechActivityEvent.hasEnded](auvoiceiospeechactivityevent/hasended.md)
  A state that indicates speech ended.
### Initializers
- [init?(rawValue: UInt32)](auvoiceiospeechactivityevent/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var kAUVoiceIOProperty_MutedSpeechActivityEventListener: AudioUnitPropertyID](kauvoiceioproperty_mutedspeechactivityeventlistener.md)
  A property to register a listener that the system calls when it detects speech while the user has the microphone muted.
- [typealias AUVoiceIOMutedSpeechActivityEventListener](auvoiceiomutedspeechactivityeventlistener.md)
  A block that the system calls to indicate speech activity while the user has the microphone muted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auvoiceiospeechactivityevent)*