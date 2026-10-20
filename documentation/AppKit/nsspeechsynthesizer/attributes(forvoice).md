# attributes(forVoice:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Provides the attribute dictionary of a voice.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
class func attributes(forVoice voice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]
```

```objc
+ (NSDictionary<NSString *,id> *) attributesForVoice:(NSSpeechSynthesizerVoiceName) voice;
```

#### Return Value

Attribute dictionary of the voice identified by `voiceIdentifier`. The attributes keys and value types are listed in `Voice Attributes Keys`

## Parameters

- `voice`: Identifier of the voice whose attributes you want to obtain.

## See Also

### Getting Speech Synthesizer Information
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](./availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](./defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](./voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](./voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](./attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/attributes(forvoice:))*