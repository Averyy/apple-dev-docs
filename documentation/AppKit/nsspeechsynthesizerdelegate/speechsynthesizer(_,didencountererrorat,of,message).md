# speechSynthesizer(_:didEncounterErrorAt:of:message:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, didEncounterErrorAt characterIndex: Int, of string: String, message: String)
```

#### Discussion

The synthesizer sends an error delegate message whenever it encounters a syntax error within a command embedded in the string it is processing. This can be useful during application debugging, to detect problems with commands that you have embedded in strings that your application speaks. It can also be useful if your application allows users to embed commands within strings. Your application might display an alert indicating that the synthesizer encountered a problem in processing an embedded command.

If your application needs information about errors that occurred prior to calling your error delegate method, the application (including the error delegate method) can call the sender’s [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) method with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) constant.

## Parameters

- `sender`: Speech synthesizer informing its delegate of an error.
- `characterIndex`: Location in text where the receiver encountered the error.
- `string`: Text the receiver was synthesizing when the error occurred.
- `message`: Error message.

## See Also

- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakWord: NSRange, of: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:).md)
  Sent just before a synthesized word is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakphoneme:).md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountersyncmessage:).md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md)
  Sent when an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object finishes speaking through the sound output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:didencountererrorat:of:message:))*