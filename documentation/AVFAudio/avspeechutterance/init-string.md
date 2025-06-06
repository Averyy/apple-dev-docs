# init(string:)

**Framework**: AVFAudio  
**Kind**: init

Creates an utterance with the text string that you specify for the speech synthesizer to speak.

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
init(string: String)
```

#### Return Value

An [`AVSpeechUtterance`](avspeechutterance.md) object that can speak the specified text.

#### Discussion

To speak the text, pass the utterance to an instance of [`AVSpeechSynthesizer`](avspeechsynthesizer.md).

## Parameters

- `string`: A string that contains the text to speak.

## See Also

- [init(attributedString: NSAttributedString)](avspeechutterance/init(attributedstring:).md)
  Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.
- [let AVSpeechSynthesisIPANotationAttribute: String](avspeechsynthesisipanotationattribute.md)
  A string that contains International Phonetic Alphabet (IPA) symbols the speech synthesizer uses to control pronunciation of certain words or phrases.
- [init?(ssmlRepresentation: String)](avspeechutterance/init(ssmlrepresentation:).md)
  Creates a speech utterance with an Speech Synthesis Markup Language (SSML) string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/init(string:))*