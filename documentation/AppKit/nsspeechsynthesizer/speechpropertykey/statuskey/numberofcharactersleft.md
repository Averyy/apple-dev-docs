# numberOfCharactersLeft

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The number of characters left in the input string of text.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let numberOfCharactersLeft: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey
```

```c
extern NSSpeechStatusKey const NSSpeechStatusNumberOfCharactersLeft;
```

## Discussion

When the value of this key is zero, you can destroy the input string.

## See Also

### Status Keys
- [static let outputBusy: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./outputbusy.md)
  Indicates whether the synthesizer is currently producing speech.
- [static let outputPaused: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./outputpaused.md)
  Indicates whether speech output in the synthesizer has been paused by sending the message [`pauseSpeaking(at:)`](../../pausespeaking%28at%29.md).
- [static let phonemeCode: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./phonemecode.md)
  Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/statuskey/numberofcharactersleft)*