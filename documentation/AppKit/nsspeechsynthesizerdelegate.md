# NSSpeechSynthesizerDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of optional methods implemented by delegates of [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) objects.

**Availability**:
- macOS 10.3+

## Declaration

```swift
protocol NSSpeechSynthesizerDelegate : NSObjectProtocol
```

## Topics

### Synthesizing Speech
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountererrorat:of:message:).md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountersyncmessage:).md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md)
  Sent when an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object finishes speaking through the sound output device.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSSpeechSynthesizerDelegate)?](nsspeechsynthesizer/delegate.md)
  The synthesizer’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate)*