# speechSynthesizer(_:willSpeakPhoneme:)

**Framework**: AppKit  
**Kind**: method

Sent just before a synthesized phoneme is spoken through the sound output device.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, willSpeakPhoneme phonemeOpcode: Int16)
```

#### Discussion

One use of this method might be to animate a mouth on screen to match the generated speech.

##### Special Considerations

This method is not sent for modern voices. It is only supported for MacinTalk voices.

In OS X v10.4 and earlier, the delegate is not sent this message when the `NSSpeechSynthesizer` object is synthesizing speech to a file ([`startSpeaking(_:to:)`](nsspeechsynthesizer/startspeaking(_:to:).md)).

## Parameters

- `sender`: An   object that’s synthesizing text into speech.
- `phonemeOpcode`: Phoneme that   is about to speak into the sound output device.

## See Also

- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountererrorat:of:message:).md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountersyncmessage:).md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md)
  Sent when an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object finishes speaking through the sound output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:))*