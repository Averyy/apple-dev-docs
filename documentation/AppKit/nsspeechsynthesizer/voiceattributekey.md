# NSSpeechSynthesizer.VoiceAttributeKey

**Framework**: AppKit  
**Kind**: struct

The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct VoiceAttributeKey
```

#### Overview

The following are the identifiers of the macOS system voices (defined in `/System/Library/Speech/Voices`):

```objc
com.apple.speech.synthesis.voice.Agnes
com.apple.speech.synthesis.voice.Albert
com.apple.speech.synthesis.voice.Alex
com.apple.speech.synthesis.voice.BadNews
com.apple.speech.synthesis.voice.Bahh
com.apple.speech.synthesis.voice.Bells
com.apple.speech.synthesis.voice.Boing
com.apple.speech.synthesis.voice.Bruce
com.apple.speech.synthesis.voice.Bubbles
com.apple.speech.synthesis.voice.Cellos
com.apple.speech.synthesis.voice.Deranged
com.apple.speech.synthesis.voice.Fred
com.apple.speech.synthesis.voice.GoodNews
com.apple.speech.synthesis.voice.Hysterical
com.apple.speech.synthesis.voice.Junior
com.apple.speech.synthesis.voice.Kathy
com.apple.speech.synthesis.voice.Organ
com.apple.speech.synthesis.voice.Princess
com.apple.speech.synthesis.voice.Ralph
com.apple.speech.synthesis.voice.Trinoids
com.apple.speech.synthesis.voice.Vicki
com.apple.speech.synthesis.voice.Victoria
com.apple.speech.synthesis.voice.Whisper
com.apple.speech.synthesis.voice.Zarvox
```

## Topics

### Voice Attribute Keys
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
- [static let individuallySpokenCharacters: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/individuallyspokencharacters.md)
  A list of Unicode character id ranges that define the Unicode characters that can be spoken in character-by-character mode by this voice.
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/voiceattributekey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](nsspeechsynthesizer/attributes(forvoice:).md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/voicename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voiceattributekey)*