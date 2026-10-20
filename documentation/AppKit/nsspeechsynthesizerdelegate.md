# NSSpeechSynthesizerDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods implemented by delegates of [`NSSpeechSynthesizer`](./nsspeechsynthesizer.md) objects.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
protocol NSSpeechSynthesizerDelegate : NSObjectProtocol
```

```objc
@protocol NSSpeechSynthesizerDelegate <NSObject>
```

## Topics

### Synthesizing Speech
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](./nsspeechsynthesizerdelegate/speechsynthesizer%28_,willspeakword,of%29.md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](./nsspeechsynthesizerdelegate/speechsynthesizer%28_,willspeakphoneme%29.md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](./nsspeechsynthesizerdelegate/speechsynthesizer%28_,didencountererrorat,of,message%29.md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](./nsspeechsynthesizerdelegate/speechsynthesizer%28_,didencountersyncmessage%29.md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](./nsspeechsynthesizerdelegate/speechsynthesizer%28_,didfinishspeaking%29.md)
  Sent when an [`NSSpeechSynthesizer`](./nsspeechsynthesizer.md) object finishes speaking through the sound output device.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the Speech Synthesizer Behavior
- [var delegate: (any NSSpeechSynthesizerDelegate)?](./nsspeechsynthesizer/delegate.md)
  The synthesizer’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate)*