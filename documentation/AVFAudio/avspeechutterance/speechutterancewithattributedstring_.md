# speechUtteranceWithAttributedString:

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Type Method

Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
+ (instancetype) speechUtteranceWithAttributedString:(NSAttributedString *) string;
```

## Return Value

An [`AVSpeechUtterance`](../avspeechutterance.md) object that can speak the specified text.

## Discussion

To speak the text, pass the utterance to an instance of [`AVSpeechSynthesizer`](../avspeechsynthesizer.md).

## Parameters

- `string`: A string that contains the text to speak.

## See Also

### Creating an utterance
- [init(string: String)](./init%28string%29.md)
  Creates an utterance with the text string that you specify for the speech synthesizer to speak.
- [+ speechUtteranceWithString:](./speechutterancewithstring_.md)
  Creates an utterance with the text string that you specify for the speech synthesizer to speak.
- [init(attributedString: NSAttributedString)](./init%28attributedstring%29.md)
  Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.
- [let AVSpeechSynthesisIPANotationAttribute: String](../avspeechsynthesisipanotationattribute.md)
  A string that contains International Phonetic Alphabet (IPA) symbols the speech synthesizer uses to control pronunciation of certain words or phrases.
- [+ speechUtteranceWithSSMLRepresentation:](./speechutterancewithssmlrepresentation_.md)
  Returns a new speech utterance with an Speech Synthesis Markup Language (SSML) string.
- [init?(ssmlRepresentation: String)](./init%28ssmlrepresentation%29-8zam9.md)
  Creates a speech utterance with an Speech Synthesis Markup Language (SSML) string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/speechutterancewithattributedstring:)*