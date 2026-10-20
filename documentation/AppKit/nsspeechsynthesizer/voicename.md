# NSSpeechSynthesizer.VoiceName

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
struct VoiceName
```

```c
typedef NSString * NSSpeechSynthesizerVoiceName;
```

## Topics

### Initializers
- [init(rawValue: String)](./voicename/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Speech Synthesizer Information
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](./availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](./attributes%28forvoice%29.md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](./defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](./attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voicename)*