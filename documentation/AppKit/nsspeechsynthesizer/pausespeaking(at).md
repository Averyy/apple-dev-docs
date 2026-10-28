# pauseSpeaking(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Pauses synthesis in progress at a given boundary.

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
func pauseSpeaking(at boundary: NSSpeechSynthesizer.Boundary)
```

```objc
- (void) pauseSpeakingAtBoundary:(NSSpeechBoundary) boundary;
```

## Discussion

Pass the constant [`NSSpeechSynthesizer.Boundary.immediateBoundary`](./boundary/immediateboundary.md) to pause immediately, even in the middle of a word. Pass [`NSSpeechSynthesizer.Boundary.wordBoundary`](./boundary/wordboundary.md) or [`NSSpeechSynthesizer.Boundary.sentenceBoundary`](./boundary/sentenceboundary.md) to pause speech at the end of the current word or sentence, respectively.

You can determine whether your application has paused a synthesizer’s speech output by obtaining the [`status`](./speechpropertykey/status.md) property through the [`object(forProperty:)`](./object%28forproperty%29.md) method. While a synthesizer is paused, the speech status information indicates that [`outputBusy`](./speechpropertykey/statuskey/outputbusy.md) and [`outputPaused`](./speechpropertykey/statuskey/outputpaused.md) are both [`true`](../../Swift/true.md).

If the end of the string being spoken is reached before the specified pause point, speech output pauses at the end of the string.

## Parameters

- `boundary`: Boundary at which to pause speech. The supported bound types are listed in [`NSSpeechSynthesizer.Boundary`](./boundary.md).

## See Also

### Synthesizing Speech
- [var isSpeaking: Bool](./isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](./startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](./startspeaking%28_,to%29.md)
  Begins synthesizing text into a sound (AIFF) file.
- [func continueSpeaking()](./continuespeaking%28%29.md)
  Resumes synthesis.
- [func stopSpeaking()](./stopspeaking%28%29.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](./stopspeaking%28at%29.md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](./boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./stopspeaking%28at%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/pausespeaking(at:))*