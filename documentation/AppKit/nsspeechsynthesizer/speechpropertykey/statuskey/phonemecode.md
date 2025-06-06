# phonemeCode

**Framework**: AppKit  
**Kind**: property

Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let phonemeCode: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey
```

## See Also

- [static let numberOfCharactersLeft: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/numberofcharactersleft.md)
  The number of characters left in the input string of text.
- [static let outputBusy: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/outputbusy.md)
  Indicates whether the synthesizer is currently producing speech.
- [static let outputPaused: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/outputpaused.md)
  Indicates whether speech output in the synthesizer has been paused by sending the message [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/statuskey/phonemecode)*