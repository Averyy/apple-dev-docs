# normal

**Framework**: AppKit  
**Kind**: property

Indicates that the synthesizer assembles digits into numbers (so that 12 is spoken as “twelve”) and text into words.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let normal: NSSpeechSynthesizer.SpeechPropertyKey.Mode
```

## See Also

- [static let literal: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/literal.md)
  Indicates that each digit or character is spoken literally (so that 12 is spoken as “one, two”, or the word “cat” is spoken as “C A T”).
- [static let phoneme: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/phoneme.md)
  Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
- [static let text: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/text.md)
  Indicates that the synthesizer is in text-processing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/mode/normal)*