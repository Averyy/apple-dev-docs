# stopSpeaking(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stops synthesis in progress at a given boundary.

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
func stopSpeaking(at boundary: NSSpeechSynthesizer.Boundary)
```

```objc
- (void) stopSpeakingAtBoundary:(NSSpeechBoundary) boundary;
```

## Discussion

Pass the constant [`NSSpeechSynthesizer.Boundary.immediateBoundary`](./boundary/immediateboundary.md) to stop immediately, even in the middle of a word. Pass [`NSSpeechSynthesizer.Boundary.wordBoundary`](./boundary/wordboundary.md) or [`NSSpeechSynthesizer.Boundary.sentenceBoundary`](./boundary/sentenceboundary.md) to stop speech at the end of the current word or sentence, respectively.

If the end of the string being spoken is reached before the specified stopping point, the synthesizer stops at the end of the string without generating an error.

## Parameters

- `boundary`: Boundary at which to stop speech. The supported bound types are listed in [`NSSpeechSynthesizer.Boundary`](./boundary.md).

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
- [func continueSpeaking()](./continuespeaking%28%29.md)
  Resumes synthesis.
- [func stopSpeaking()](./stopspeaking%28%29.md)
  Stops synthesis in progress.
- [NSSpeechSynthesizer.Boundary](./boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./stopspeaking%28at%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/stopspeaking(at:))*