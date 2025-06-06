# speechSynthesizer(_:didFinishSpeaking:)

**Framework**: AppKit  
**Kind**: method

Sent when an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object finishes speaking through the sound output device.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, didFinishSpeaking finishedSpeaking: Bool)
```

## Parameters

- `sender`: An   object that has stopped speaking into the sound output device.
- `finishedSpeaking`:   when speaking completed normally,   if speaking is stopped prematurely for any reason.

## See Also

- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func stopSpeaking()](nsspeechsynthesizer/stopspeaking.md)
  Stops synthesis in progress.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountererrorat:of:message:).md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountersyncmessage:).md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:))*