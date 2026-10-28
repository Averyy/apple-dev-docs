# isSpeaking

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the receiver is currently generating synthesized speech.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
var isSpeaking: Bool { get }
```

```objc
@property (readonly, getter=isSpeaking) BOOL speaking;
```

## Discussion

[`true`](../../Swift/true.md) when the receiver is generating synthesized speech, [`false`](../../Swift/false.md) otherwise.

## See Also

### Synthesizing Speech
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
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](./stopspeaking%28at%29.md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](./boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./stopspeaking%28at%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/isspeaking)*