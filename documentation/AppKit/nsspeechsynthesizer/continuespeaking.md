# continueSpeaking()

**Framework**: AppKit  
**Kind**: method

Resumes synthesis.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func continueSpeaking()
```

#### Discussion

At any time after [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) is called, [`continueSpeaking()`](nsspeechsynthesizer/continuespeaking().md) can be called to continue speaking from the beginning of the word at which speech paused.

Sending [`continueSpeaking()`](nsspeechsynthesizer/continuespeaking().md) to a receiver that is not currently in a paused state has no effect on the synthesizer or on future calls to the [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) function. If you call [`continueSpeaking()`](nsspeechsynthesizer/continuespeaking().md) on a synthesizer before a pause is effective, [`continueSpeaking()`](nsspeechsynthesizer/continuespeaking().md) cancels the pause.

If the [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) method stopped speech in the middle of a word, the synthesizer will start speaking that word from the beginning when you call [`continueSpeaking()`](nsspeechsynthesizer/continuespeaking().md).

## See Also

- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](nsspeechsynthesizer/startspeaking(_:to:).md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/pausespeaking(at:).md)
  Pauses synthesis in progress at a given boundary.
- [func stopSpeaking()](nsspeechsynthesizer/stopspeaking.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/stopspeaking(at:).md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/continuespeaking())*