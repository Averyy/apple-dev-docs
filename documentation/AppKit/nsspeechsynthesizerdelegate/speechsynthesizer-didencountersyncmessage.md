# speechSynthesizer(_:didEncounterSyncMessage:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate when a speech synthesizer encounters a synchronization error.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, didEncounterSyncMessage message: String)
```

#### Discussion

The synthesizer calls your synchronization delegate method whenever it encounters a synchronization command embedded in a string. You might use the synchronization delegate method to provide a callback not ordinarily provided.

For example, you might insert synchronization commands at the end of every sentence in a string, or you might enter synchronization commands after every numeric value in the text.

However, to synchronize your application with phonemes or words, it makes more sense to use the built-in phoneme and word delegate methods: [`speechSynthesizer(_:willSpeakPhoneme:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md) and [`speechSynthesizer(_:willSpeakWord:of:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md).

## Parameters

- `sender`: Speech synthesizer informing its delegate of an error.
- `message`: Error message.

## See Also

- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountererrorat:of:message:).md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md)
  Sent when an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object finishes speaking through the sound output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountersyncmessage:))*