# demoText

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A demonstration string to speak. An `NSString`

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
static let demoText: NSSpeechSynthesizer.VoiceAttributeKey
```

```c
extern NSVoiceAttributeKey const NSVoiceDemoText;
```

## See Also

### Voice Attribute Keys
- [static let identifier: NSSpeechSynthesizer.VoiceAttributeKey](./identifier.md)
  A unique string identifying the voice. The identifiers of the system voices are listed in `Listing 1`.
- [static let name: NSSpeechSynthesizer.VoiceAttributeKey](./name.md)
  The name of the voice suitable for display. An `NSString`.
- [static let age: NSSpeechSynthesizer.VoiceAttributeKey](./age.md)
  The perceived age (in years) of the voice. An `NSString`
- [static let gender: NSSpeechSynthesizer.VoiceAttributeKey](./gender.md)
  The perceived gender of the voice. The supported values are listed in `Voice Gender Keys`.  An `NSString`
- [static let localeIdentifier: NSSpeechSynthesizer.VoiceAttributeKey](./localeidentifier.md)
  The language of the voice.  An `NSString`
- [static let supportedCharacters: NSSpeechSynthesizer.VoiceAttributeKey](./supportedcharacters.md)
  A list of Unicode character id ranges that define the Unicode characters supported by this voice.
- [static let individuallySpokenCharacters: NSSpeechSynthesizer.VoiceAttributeKey](./individuallyspokencharacters.md)
  A list of Unicode character id ranges that define the Unicode characters that can be spoken in character-by-character mode by this voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voiceattributekey/demotext)*