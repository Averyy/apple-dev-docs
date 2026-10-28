# outputBusy

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Indicates whether the synthesizer is currently producing speech.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let outputBusy: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey
```

```c
extern NSSpeechStatusKey const NSSpeechStatusOutputBusy;
```

## Discussion

A synthesizer is considered to be producing speech even at some times when no audio data is being produced through the computer’s speaker. This occurs, for example, when the synthesizer is processing input, but has not yet initiated speech or when speech output is paused.

## See Also

### Status Keys
- [static let numberOfCharactersLeft: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./numberofcharactersleft.md)
  The number of characters left in the input string of text.
- [static let outputPaused: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./outputpaused.md)
  Indicates whether speech output in the synthesizer has been paused by sending the message [`pauseSpeaking(at:)`](../../pausespeaking%28at%29.md).
- [static let phonemeCode: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./phonemecode.md)
  Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/statuskey/outputbusy)*