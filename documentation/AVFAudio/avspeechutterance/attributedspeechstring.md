# attributedSpeechString

**Framework**: AVFAudio  
**Kind**: property

An attributed string that contains the text for speech synthesis.

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
var attributedSpeechString: NSAttributedString { get }
```

#### Discussion

You can’t change an utterance’s text after initializaiton. If you want the speech synthesizer to speak different text, create a new utterance.

## See Also

- [var speechString: String](avspeechutterance/speechstring.md)
  A string that contains the text for speech synthesis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/attributedspeechstring)*