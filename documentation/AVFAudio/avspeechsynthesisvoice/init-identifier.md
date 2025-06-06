# init(identifier:)

**Framework**: AVFAudio  
**Kind**: init

Retrieves a voice for the identifier you specify.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(identifier: String)
```

#### Return Value

A voice for the specified identifier if the identifier is valid and the voice is available on the device; otherwise, `nil`.

## Parameters

- `identifier`: The unique identifier for a voice.

## See Also

- [init?(language: String?)](avspeechsynthesisvoice/init(language:).md)
  Retrieves a voice for the BCP 47 code language code you specify.
- [class func speechVoices() -> [AVSpeechSynthesisVoice]](avspeechsynthesisvoice/speechvoices.md)
  Retrieves all available voices on the device.
- [let AVSpeechSynthesisVoiceIdentifierAlex: String](avspeechsynthesisvoiceidentifieralex.md)
  The voice that the system identifies as Alex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/init(identifier:))*