# continueSpeaking()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Resumes synthesis.

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
func continueSpeaking()
```

```objc
- (void) continueSpeaking;
```

## Discussion

At any time after [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) is called, [`continueSpeaking()`](./continuespeaking%28%29.md) can be called to continue speaking from the beginning of the word at which speech paused.

Sending [`continueSpeaking()`](./continuespeaking%28%29.md) to a receiver that is not currently in a paused state has no effect on the synthesizer or on future calls to the [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) function. If you call [`continueSpeaking()`](./continuespeaking%28%29.md) on a synthesizer before a pause is effective, [`continueSpeaking()`](./continuespeaking%28%29.md) cancels the pause.

If the [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) method stopped speech in the middle of a word, the synthesizer will start speaking that word from the beginning when you call [`continueSpeaking()`](./continuespeaking%28%29.md).

## See Also

### Synthesizing Speech
- [var isSpeaking: Bool](./isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](./startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](./startspeaking%28_,to%29.md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](./pausespeaking%28at%29.md)
  Pauses synthesis in progress at a given boundary.
- [func stopSpeaking()](./stopspeaking%28%29.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](./stopspeaking%28at%29.md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](./boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./stopspeaking%28at%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/continuespeaking())*