# speechVoices()

**Framework**: AVFAudio  
**Kind**: method

Retrieves all available voices on the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func speechVoices() -> [AVSpeechSynthesisVoice]
```

#### Return Value

An array of voices.

#### Discussion

Use the [`language`](avspeechsynthesisvoice/language.md) property to identify each voice by its language and locale.

## See Also

- [init?(identifier: String)](avspeechsynthesisvoice/init(identifier:).md)
  Retrieves a voice for the identifier you specify.
- [init?(language: String?)](avspeechsynthesisvoice/init(language:).md)
  Retrieves a voice for the BCP 47 code language code you specify.
- [let AVSpeechSynthesisVoiceIdentifierAlex: String](avspeechsynthesisvoiceidentifieralex.md)
  The voice that the system identifies as Alex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/speechvoices())*