# individuallySpokenCharacters

**Framework**: AppKit  
**Kind**: property

A list of Unicode character id ranges that define the Unicode characters that can be spoken in character-by-character mode by this voice.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let individuallySpokenCharacters: NSSpeechSynthesizer.VoiceAttributeKey
```

#### Discussion

Each list entry is a dictionary containing two keys: “UnicodeCharBegin”, an integer value containing the beginning Unicode id of this range; and “UnicodeCharEnd”, an integer value containing the ending Unicode id of this range. Your application can use these ranges to determine if the voice can speak the name of an individual character when spoken in character-by-character mode.

Some voices may not provide this attribute.

## See Also

- [static let identifier: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/identifier.md)
  A unique string identifying the voice. The identifiers of the system voices are listed in `Listing 1`.
- [static let name: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/name.md)
  The name of the voice suitable for display. An `NSString`.
- [static let age: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/age.md)
  The perceived age (in years) of the voice. An `NSString`
- [static let gender: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/gender.md)
  The perceived gender of the voice. The supported values are listed in `Voice Gender Keys`.  An `NSString`
- [static let demoText: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/demotext.md)
  A demonstration string to speak. An `NSString`
- [static let localeIdentifier: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/localeidentifier.md)
  The language of the voice.  An `NSString`
- [static let supportedCharacters: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/supportedcharacters.md)
  A list of Unicode character id ranges that define the Unicode characters supported by this voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voiceattributekey/individuallyspokencharacters)*