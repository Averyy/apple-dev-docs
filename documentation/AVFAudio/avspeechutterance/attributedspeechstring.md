# attributedSpeechString

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSAttributedString * attributedSpeechString;
```

#### Discussion

You can’t change an utterance’s text after initializaiton. If you want the speech synthesizer to speak different text, create a new utterance.

## See Also

### Inspecting utterance text
- [var speechString: String](./speechstring.md)
  A string that contains the text for speech synthesis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechutterance/attributedspeechstring)*