# stopSpeaking()

**Framework**: AppKit  
**Kind**: method

Stops synthesis in progress.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func stopSpeaking()
```

#### Discussion

If the receiver is currently generating speech, synthesis is halted, and the message [`speechSynthesizer(_:didFinishSpeaking:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md) is sent to the delegate.

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
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/stopspeaking(at:).md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/stopspeaking())*