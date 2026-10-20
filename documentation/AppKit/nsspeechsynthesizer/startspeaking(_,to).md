# startSpeaking(_:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Begins synthesizing text into a sound (AIFF) file.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
func startSpeaking(_ string: String, to url: URL) -> Bool
```

```objc
- (BOOL) startSpeakingString:(NSString *) string toURL:(NSURL *) url;
```

#### Return Value

[`true`](../../Swift/true.md) when synthesis starts successfully, [`false`](../../Swift/false.md) otherwise.

#### Discussion

When synthesis of `text` finishes normally or is stopped, the message [`speechSynthesizer(_:didFinishSpeaking:)`](../nsspeechsynthesizerdelegate/speechsynthesizer%28_,didfinishspeaking%29.md) is sent to the delegate.

One example of how you might use this method is in an email program that automatically converts new messages into sound files that can be stored on an iPod for later listening.

> **Note**:  In OS X V 10.4 and earlier, the delegate does not receive [`speechSynthesizer(_:willSpeakWord:of:)`](../nsspeechsynthesizerdelegate/speechsynthesizer%28_,willspeakword,of%29.md) and [`speechSynthesizer(_:willSpeakPhoneme:)`](../nsspeechsynthesizerdelegate/speechsynthesizer%28_,willspeakphoneme%29.md) messages when text is being synthesized to a file.

## Parameters

- `string`: Text to speak. When `nil` or empty, no synthesis is started.
- `url`: Filesystem location of the output sound file.

## See Also

### Synthesizing Speech
- [var isSpeaking: Bool](./isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](./startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](./pausespeaking%28at%29.md)
  Pauses synthesis in progress at a given boundary.
- [func continueSpeaking()](./continuespeaking%28%29.md)
  Resumes synthesis.
- [func stopSpeaking()](./stopspeaking%28%29.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](./stopspeaking%28at%29.md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](./boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./stopspeaking%28at%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/startspeaking(_:to:))*