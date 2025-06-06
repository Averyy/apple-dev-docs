# startSpeaking(_:to:)

**Framework**: Appkit  
**Kind**: method

Begins synthesizing text into a sound (AIFF) file.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func startSpeaking(_ string: String, to url: URL) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) when synthesis starts successfully, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

When synthesis of `text` finishes normally or is stopped, the message [`speechSynthesizer(_:didFinishSpeaking:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md) is sent to the delegate.

One example of how you might use this method is in an email program that automatically converts new messages into sound files that can be stored on an iPod for later listening.

> **Note**:  In OS X V 10.4 and earlier, the delegate does not receive [`speechSynthesizer(_:willSpeakWord:of:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md) and [`speechSynthesizer(_:willSpeakPhoneme:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md) messages when text is being synthesized to a file.

## Parameters

- `string`: Text to speak. When   or empty, no synthesis is started.
- `url`: Filesystem location of the output sound file.

## See Also

- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/startspeaking(_:to:))*