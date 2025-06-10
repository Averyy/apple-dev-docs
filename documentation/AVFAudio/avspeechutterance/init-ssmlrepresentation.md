# init(ssmlRepresentation:)

**Framework**: AVFAudio  
**Kind**: init

Creates a speech utterance with an Speech Synthesis Markup Language (SSML) string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init?(ssmlRepresentation string: String)
```

#### Discussion

If using SSML to request voices that fall under certain attributes, the system may split a single utterance into multiple parts and send each to an appropriate synthesizer.

If no voice matches the properties, the utterance uses the voice set in its [`voice`](avspeechutterance/voice.md) property. If you don’t specify a voice, the system uses its default voice.

> **Note**:  Speech utterance properties that affect the prosody of a voice, such as its [`rate`](avspeechutterance/rate.md) and [`pitchMultiplier`](avspeechutterance/pitchmultiplier.md), don’t apply to an utterance that uses an SSML representation.

## Parameters

- `string`: A string to speak that contains valid SSML markup. The initializer returns   if you pass an invalid SSML string.

## See Also

- [init(string: String)](avspeechutterance/init(string:).md)
  Creates an utterance with the text string that you specify for the speech synthesizer to speak.
- [init(attributedString: NSAttributedString)](avspeechutterance/init(attributedstring:).md)
  Creates an utterance with the attributed text string that you specify for the speech synthesizer to speak.
- [let AVSpeechSynthesisIPANotationAttribute: String](avspeechsynthesisipanotationattribute.md)
  A string that contains International Phonetic Alphabet (IPA) symbols the speech synthesizer uses to control pronunciation of certain words or phrases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/init(ssmlrepresentation:))*