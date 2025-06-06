# speechString

**Framework**: AVFAudio  
**Kind**: property

A string that contains the text for speech synthesis.

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
var speechString: String { get }
```

#### Discussion

You can’t change an utterance’s text after initializaiton. If you want the speech synthesizer to speak different text, create a new utterance.

## See Also

- [var attributedSpeechString: NSAttributedString](avspeechutterance/attributedspeechstring.md)
  An attributed string that contains the text for speech synthesis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/speechstring)*