# availableVoices

**Framework**: AppKit  
**Kind**: property

Provides the identifiers of the voices available on the system.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class var availableVoices: [NSSpeechSynthesizer.VoiceName] { get }
```

#### Return Value

Array of strings representing the identifiers of each voice available on the system.

## See Also

- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](nsspeechsynthesizer/setvoice(_:).md)
  Sets the receiver’s current voice.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](nsspeechsynthesizer/attributes(forvoice:).md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/availablevoices)*