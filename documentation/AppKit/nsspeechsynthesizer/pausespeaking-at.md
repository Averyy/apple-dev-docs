# pauseSpeaking(at:)

**Framework**: AppKit  
**Kind**: method

Pauses synthesis in progress at a given boundary.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func pauseSpeaking(at boundary: NSSpeechSynthesizer.Boundary)
```

#### Discussion

Pass the constant [`NSSpeechSynthesizer.Boundary.immediateBoundary`](nsspeechsynthesizer/boundary/immediateboundary.md) to pause immediately, even in the middle of a word. Pass [`NSSpeechSynthesizer.Boundary.wordBoundary`](nsspeechsynthesizer/boundary/wordboundary.md) or [`NSSpeechSynthesizer.Boundary.sentenceBoundary`](nsspeechsynthesizer/boundary/sentenceboundary.md) to pause speech at the end of the current word or sentence, respectively.

You can determine whether your application has paused a synthesizer’s speech output by obtaining the [`status`](nsspeechsynthesizer/speechpropertykey/status.md) property through the [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) method. While a synthesizer is paused, the speech status information indicates that [`outputBusy`](nsspeechsynthesizer/speechpropertykey/statuskey/outputbusy.md) and [`outputPaused`](nsspeechsynthesizer/speechpropertykey/statuskey/outputpaused.md) are both [`true`](https://developer.apple.com/documentation/swift/true).

If the end of the string being spoken is reached before the specified pause point, speech output pauses at the end of the string.

## Parameters

- `boundary`: Boundary at which to pause speech. The supported bound types are listed in  .

## See Also

- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](nsspeechsynthesizer/startspeaking(_:to:).md)
  Begins synthesizing text into a sound (AIFF) file.
- [func continueSpeaking()](nsspeechsynthesizer/continuespeaking.md)
  Resumes synthesis.
- [func stopSpeaking()](nsspeechsynthesizer/stopspeaking.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/stopspeaking(at:).md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/pausespeaking(at:))*