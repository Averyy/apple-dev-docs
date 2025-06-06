# attributes(forVoice:)

**Framework**: AppKit  
**Kind**: method

Provides the attribute dictionary of a voice.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class func attributes(forVoice voice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]
```

#### Return Value

Attribute dictionary of the voice identified by `voiceIdentifier`. The attributes keys and value types are listed in `Voice Attributes Keys`

## Parameters

- `voice`: Identifier of the voice whose attributes you want to obtain.

## See Also

- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/attributes(forvoice:))*