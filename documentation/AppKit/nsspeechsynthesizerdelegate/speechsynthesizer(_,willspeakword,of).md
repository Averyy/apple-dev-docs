# speechSynthesizer(_:willSpeakWord:of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent just before a synthesized word is spoken through the sound output device.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
@MainActor
optional func speechSynthesizer(_ sender: NSSpeechSynthesizer, willSpeakWord characterRange: NSRange, of string: String)
```

```objc
- (void) speechSynthesizer:(NSSpeechSynthesizer *) sender willSpeakWord:(NSRange) characterRange ofString:(NSString *) string;
```

#### Discussion

One use of this method might be to visually highlight the word being spoken.

> ❗ **Important**:  In OS X v10.4 and earlier, the delegate is not sent this message when the `NSSpeechSynthesizer` object is synthesizing speech to a file ([`startSpeaking(_:to:)`](../nsspeechsynthesizer/startspeaking%28_,to%29.md)).

## Parameters

- `sender`: An [`NSSpeechSynthesizer`](../nsspeechsynthesizer.md) object that’s synthesizing text into speech.
- `characterRange`: Word that `sender` is about to speak into the sound output device.
- `string`: Text that is being synthesized by `sender`.

## See Also

### Related Documentation
- [func startSpeaking(String) -> Bool](../nsspeechsynthesizer/startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
### Synthesizing Speech
- [func speechSynthesizer(NSSpeechSynthesizer, willSpeakPhoneme: Int16)](./speechsynthesizer%28_,willspeakphoneme%29.md)
  Sent just before a synthesized phoneme is spoken through the sound output device.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterErrorAt: Int, of: String, message: String)](./speechsynthesizer%28_,didencountererrorat,of,message%29.md)
  Sent to the delegate when a speech synthesizer encounters an error in text being synthesized.
- [func speechSynthesizer(NSSpeechSynthesizer, didEncounterSyncMessage: String)](./speechsynthesizer%28_,didencountersyncmessage%29.md)
  Sent to the delegate when a speech synthesizer encounters a synchronization error.
- [func speechSynthesizer(NSSpeechSynthesizer, didFinishSpeaking: Bool)](./speechsynthesizer%28_,didfinishspeaking%29.md)
  Sent when an [`NSSpeechSynthesizer`](../nsspeechsynthesizer.md) object finishes speaking through the sound output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizerdelegate/speechsynthesizer(_:willspeakword:of:))*