# init(language:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Retrieves a voice for the BCP 47 code language code you specify.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(language languageCode: String?)
```

```objc
+ (AVSpeechSynthesisVoice *) voiceWithLanguage:(NSString *) languageCode;
```

#### Return Value

A voice for the specified language and locale code if the code is valid; otherwise, `nil`.

#### Discussion

- languageCode: A BCP 47 code that identifies the language and locale for a voice.

#### Discussion

Pass `nil` for `languageCode` to receive the default voice for the system’s language and region.

## See Also

### Creating a voice
- [init?(identifier: String)](./init%28identifier%29.md)
  Retrieves a voice for the identifier you specify.
- [class func speechVoices() -> [AVSpeechSynthesisVoice]](./speechvoices%28%29.md)
  Retrieves all available voices on the device.
- [let AVSpeechSynthesisVoiceIdentifierAlex: String](../avspeechsynthesisvoiceidentifieralex.md)
  The voice that the system identifies as Alex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice/init(language:))*