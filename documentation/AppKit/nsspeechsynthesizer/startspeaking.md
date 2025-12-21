# startSpeaking(_:)

**Framework**: AppKit  
**Kind**: method

Begins speaking synthesized text through the system’s default sound output device.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func startSpeaking(_ string: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when speaking starts successfully, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

If the receiver is currently speaking synthesized speech when [`startSpeaking(_:)`](nsspeechsynthesizer/startspeaking(_:).md) is called, that process is stopped before `text` is spoken.

When synthesis of `text` finishes normally or is stopped, the message [`speechSynthesizer(_:didFinishSpeaking:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md) is sent to the delegate.

## Parameters

- `string`: Text to speak. When   or empty, no synthesis occurs.

## See Also

- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/startspeaking(_:))*