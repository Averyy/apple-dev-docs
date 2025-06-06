# language

**Framework**: AVFAudio  
**Kind**: property

A BCP 47 code that contains the voice’s language and locale.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var language: String { get }
```

#### Discussion

The language of a voice controls the conversion of text to spoken phonemes. For best results, ensure that the language of an utterance’s text matches the voice for the utterance. The locale of a voice reflects regional variations in pronunciation or accent. For example, a voice with a language code of `en-US` speaks English text with a North American accent, and a language code of `en-AU` speaks English text with an Australian accent.

## See Also

- [class func currentLanguageCode() -> String](avspeechsynthesisvoice/currentlanguagecode.md)
  Returns the language and locale code for the user’s current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/language)*