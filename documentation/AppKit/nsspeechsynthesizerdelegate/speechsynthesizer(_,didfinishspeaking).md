# speechSynthesizer(_:didFinishSpeaking:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent when an [`NSSpeechSynthesizer`](../nsspeechsynthesizer.md) object finishes speaking through the sound output device.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, didFinishSpeaking finishedSpeaking: Bool)
```

```objc
- (void) speechSynthesizer:(NSSpeechSynthesizer *) sender didFinishSpeaking:(BOOL) finishedSpeaking;
```

## Parameters

- `sender`: An [`NSSpeechSynthesizer`](../nsspeechsynthesizer.md) object that has stopped speaking into the sound output device.
- `finishedSpeaking`: [`true`](../../Swift/true.md) when speaking completed normally, [`false`](../../Swift/false.md) if speaking is stopped prematurely for any reason.

## See Also

### Related Documentation
- [func startSpeaking(String) -> Bool](../nsspeechsynthesizer/startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func stopSpeaking()](../nsspeechsynthesizer/stopspeaking%28%29.md)
  Stops synthesis in progress.
### Synthesizing Speech
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](./speechsynthesizer%28_,willspeakword,of%29.md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](./speechsynthesizer%28_,willspeakphoneme%29.md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](./speechsynthesizer%28_,didencountererrorat,of,message%29.md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](./speechsynthesizer%28_,didencountersyncmessage%29.md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:))*