# speechSynthesizer(_:willSpeakWord:of:)

**Framework**: AppKit  
**Kind**: method

Sent just before a synthesized word is spoken through the sound output device.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, willSpeakWord characterRange: NSRange, of string: String)
```

#### Discussion

One use of this method might be to visually highlight the word being spoken.

> ❗ **Important**:  In OS X v10.4 and earlier, the delegate is not sent this message when the `NSSpeechSynthesizer` object is synthesizing speech to a file ([`startSpeaking(_:to:)`](nsspeechsynthesizer/startspeaking(_:to:).md)).

 In OS X v10.4 and earlier, the delegate is not sent this message when the `NSSpeechSynthesizer` object is synthesizing speech to a file ([`startSpeaking(_:to:)`](nsspeechsynthesizer/startspeaking(_:to:).md)).

## Parameters

- `sender`: An   object that’s synthesizing text into speech.
- `characterRange`: Word that   is about to speak into the sound output device.
- `string`: Text that is being synthesized by  .

## See Also

- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [Speech Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Speech/Speech.html#//apple_ref/doc/uid/10000178i)
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountererrorat:of:message:).md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountersyncmessage:).md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md)
  Sent when an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object finishes speaking through the sound output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:))*