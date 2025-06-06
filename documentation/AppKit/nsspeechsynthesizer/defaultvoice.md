# defaultVoice

**Framework**: AppKit  
**Kind**: property

Provides the identifier of the default voice.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class var defaultVoice: NSSpeechSynthesizer.VoiceName { get }
```

#### Return Value

Identifier of the default voice.

## See Also

- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](nsspeechsynthesizer/attributes(forvoice:).md)
  Provides the attribute dictionary of a voice.
- [NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/defaultvoice)*