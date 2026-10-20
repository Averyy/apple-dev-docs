# AVSpeechSynthesisIPANotationAttribute

**Framework**: AVFAudio  
**Kind**: var  
**Role**: Global Variable

A string that contains International Phonetic Alphabet (IPA) symbols the speech synthesizer uses to control pronunciation of certain words or phrases.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let AVSpeechSynthesisIPANotationAttribute: String
```

```c
extern NSString * const AVSpeechSynthesisIPANotationAttribute;
```

#### Discussion

For example, the speech synthesizer uses an `AVSpeechSynthesisIPANotationAttribute` instance to control pronunciation of a proper name.

## See Also

### Creating an utterance
- [init(string: String)](./avspeechutterance/init%28string%29.md)
  Creates an utterance with the text string that you specify for the speech synthesizer to speak.
- [init(attributedString: NSAttributedString)](./avspeechutterance/init%28attributedstring%29.md)
  Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.
- [init?(ssmlRepresentation: String)](./avspeechutterance/init%28ssmlrepresentation%29-8zam9.md)
  Creates a speech utterance with an Speech Synthesis Markup Language (SSML) string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisipanotationattribute)*