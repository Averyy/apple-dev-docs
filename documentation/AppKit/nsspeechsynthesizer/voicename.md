# NSSpeechSynthesizer.VoiceName

**Framework**: AppKit  
**Kind**: struct

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct VoiceName
```

## Topics

### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/voicename/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](nsspeechsynthesizer/attributes(forvoice:).md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voicename)*