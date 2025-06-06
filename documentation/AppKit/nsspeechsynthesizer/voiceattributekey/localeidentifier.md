# localeIdentifier

**Framework**: AppKit  
**Kind**: property

The language of the voice.  An `NSString`

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let localeIdentifier: NSSpeechSynthesizer.VoiceAttributeKey
```

#### Discussion

The canonical locale identifier string describing the voice’s locale. A locale is generally composed of three pieces of ordered information: a language code, a region code, and a variant code.  Refer to documentation about the [`NSLocale`](https://developer.apple.com/documentation/Foundation/NSLocale) class or [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for more information.

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
- [static let supportedCharacters: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/supportedcharacters.md)
  A list of Unicode character id ranges that define the Unicode characters supported by this voice.
- [static let individuallySpokenCharacters: NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey/individuallyspokencharacters.md)
  A list of Unicode character id ranges that define the Unicode characters that can be spoken in character-by-character mode by this voice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/voiceattributekey/localeidentifier)*