# isSpeaking

**Framework**: AppKit  
**Kind**: property

Indicates whether the receiver is currently generating synthesized speech.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var isSpeaking: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) when the receiver is generating synthesized speech, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

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
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/stopspeaking(at:).md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/isspeaking)*