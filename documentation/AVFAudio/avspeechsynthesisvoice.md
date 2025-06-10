# AVSpeechSynthesisVoice

**Framework**: AVFAudio  
**Kind**: class

A distinct voice for use in speech synthesis.

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
class AVSpeechSynthesisVoice
```

#### Overview

The primary factors that distinguish a voice in speech synthesis are language, locale, and quality. Create an instance of `AVSpeechSynthesisVoice` to select a voice that’s appropriate for the text and the language, and set it as the value of the [`voice`](avspeechutterance/voice.md) property on an [`AVSpeechUtterance`](avspeechutterance.md) instance. The voice may optionally reflect a local variant of the language, such as Australian or South African English. For a complete list of supported languages, see [`Languages Supported by VoiceOver`](https://developer.apple.comhttps://support.apple.com/en-us/HT206175).

## Topics

### Obtaining voices
- [init?(identifier: String)](avspeechsynthesisvoice/init(identifier:).md)
  Retrieves a voice for the identifier you specify.
- [init?(language: String?)](avspeechsynthesisvoice/init(language:).md)
  Retrieves a voice for the BCP 47 code language code you specify.
- [class func speechVoices() -> [AVSpeechSynthesisVoice]](avspeechsynthesisvoice/speechvoices.md)
  Retrieves all available voices on the device.
- [let AVSpeechSynthesisVoiceIdentifierAlex: String](avspeechsynthesisvoiceidentifieralex.md)
  The voice that the system identifies as Alex.
### Inspecting voices
- [var identifier: String](avspeechsynthesisvoice/identifier.md)
  The unique identifier of a voice.
- [var name: String](avspeechsynthesisvoice/name.md)
  The name of a voice.
- [var quality: AVSpeechSynthesisVoiceQuality](avspeechsynthesisvoice/quality.md)
  The speech quality of a voice.
- [var gender: AVSpeechSynthesisVoiceGender](avspeechsynthesisvoice/gender.md)
  The gender for a voice.
- [var voiceTraits: AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/voicetraits.md)
  The traits of a voice.
- [var audioFileSettings: [String : Any]](avspeechsynthesisvoice/audiofilesettings.md)
  A dictionary that contains audio file settings.
- [enum AVSpeechSynthesisVoiceQuality](avspeechsynthesisvoicequality.md)
  The speech quality of a voice.
- [enum AVSpeechSynthesisVoiceGender](avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [AVSpeechSynthesisVoice.Traits](avspeechsynthesisvoice/traits.md)
  Traits that describe a voice.
### Working with language codes
- [class func currentLanguageCode() -> String](avspeechsynthesisvoice/currentlanguagecode.md)
  Returns the language and locale code for the user’s current locale.
- [var language: String](avspeechsynthesisvoice/language.md)
  A BCP 47 code that contains the voice’s language and locale.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AVSpeechUtterance](avspeechutterance.md)
  An object that encapsulates the text for speech synthesis and parameters that affect the speech.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisvoice)*