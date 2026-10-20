# AVAudioVoiceProcessingSpeechActivityEvent

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Types of speech activity events.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum AVAudioVoiceProcessingSpeechActivityEvent
```

```c
enum AVAudioVoiceProcessingSpeechActivityEvent : NSInteger;
```

## Topics

### Creating an activity event
- [init?(rawValue: Int)](./avaudiovoiceprocessingspeechactivityevent/init%28rawvalue%29.md)
### Identifying activity events
- [AVAudioVoiceProcessingSpeechActivityEvent.started](./avaudiovoiceprocessingspeechactivityevent/started.md)
  Indicates the start of speech activity.
- [AVAudioVoiceProcessingSpeechActivityEvent.ended](./avaudiovoiceprocessingspeechactivityevent/ended.md)
  Indicates the end of speech activity.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling muted speech events
- [func setMutedSpeechActivityEventListener(((AVAudioVoiceProcessingSpeechActivityEvent) -> Void)?) -> Bool](./avaudioinputnode/setmutedspeechactivityeventlistener%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiovoiceprocessingspeechactivityevent)*