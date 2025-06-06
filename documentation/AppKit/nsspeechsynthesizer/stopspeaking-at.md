# stopSpeaking(at:)

**Framework**: AppKit  
**Kind**: method

Stops synthesis in progress at a given boundary.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func stopSpeaking(at boundary: NSSpeechSynthesizer.Boundary)
```

#### Discussion

Pass the constant [`NSSpeechSynthesizer.Boundary.immediateBoundary`](nsspeechsynthesizer/boundary/immediateboundary.md) to stop immediately, even in the middle of a word. Pass [`NSSpeechSynthesizer.Boundary.wordBoundary`](nsspeechsynthesizer/boundary/wordboundary.md) or [`NSSpeechSynthesizer.Boundary.sentenceBoundary`](nsspeechsynthesizer/boundary/sentenceboundary.md) to stop speech at the end of the current word or sentence, respectively.

If the end of the string being spoken is reached before the specified stopping point, the synthesizer stops at the end of the string without generating an error.

## Parameters

- `boundary`: Boundary at which to stop speech. The supported bound types are listed in  .

## See Also

- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](nsspeechsynthesizer/startspeaking(_:to:).md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/pausespeaking(at:).md)
  Pauses synthesis in progress at a given boundary.
- [func continueSpeaking()](nsspeechsynthesizer/continuespeaking.md)
  Resumes synthesis.
- [func stopSpeaking()](nsspeechsynthesizer/stopspeaking.md)
  Stops synthesis in progress.
- [NSSpeechSynthesizer.Boundary](nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/stopspeaking(at:))*