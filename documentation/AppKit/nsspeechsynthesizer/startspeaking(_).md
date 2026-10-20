# startSpeaking(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Begins speaking synthesized text through the system’s default sound output device.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
func startSpeaking(_ string: String) -> Bool
```

```objc
- (BOOL) startSpeakingString:(NSString *) string;
```

#### Return Value

[`true`](../../Swift/true.md) when speaking starts successfully, [`false`](../../Swift/false.md) otherwise.

#### Discussion

If the receiver is currently speaking synthesized speech when [`startSpeaking(_:)`](./startspeaking%28_%29.md) is called, that process is stopped before `text` is spoken.

When synthesis of `text` finishes normally or is stopped, the message [`speechSynthesizer(_:didFinishSpeaking:)`](../nsspeechsynthesizerdelegate/speechsynthesizer%28_,didfinishspeaking%29.md) is sent to the delegate.

## Parameters

- `string`: Text to speak. When `nil` or empty, no synthesis occurs.

## See Also

### Synthesizing Speech
- [var isSpeaking: Bool](./isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String, to: URL) -> Bool](./startspeaking%28_,to%29.md)
  Begins synthesizing text into a sound (AIFF) file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/startspeaking(_:))*