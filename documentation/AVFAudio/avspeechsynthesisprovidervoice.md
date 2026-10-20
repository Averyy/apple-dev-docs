# AVSpeechSynthesisProviderVoice

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that represents a voice that an audio unit provides to its host.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class AVSpeechSynthesisProviderVoice
```

```objc
@interface AVSpeechSynthesisProviderVoice : NSObject
```

#### Overview

This is a voice that an [`AVSpeechSynthesisProviderAudioUnit`](./avspeechsynthesisprovideraudiounit.md) provides to the system, distinct from [`AVSpeechSynthesisVoice`](./avspeechsynthesisvoice.md). Use [`speechVoices`](./avspeechsynthesisprovideraudiounit/speechvoices.md) to access the underlying [`AVSpeechSynthesisVoice`](./avspeechsynthesisvoice.md) in the voice quality [`AVSpeechSynthesisVoiceQuality.enhanced`](./avspeechsynthesisvoicequality/enhanced.md).

## Topics

### Creating a voice
- [init(name: String, identifier: String, primaryLanguages: [String], supportedLanguages: [String])](./avspeechsynthesisprovidervoice/init%28name,identifier,primarylanguages,supportedlanguages%29.md)
  Creates a voice with a name, an identifier, and language information.
### Inspecting a voice
- [var age: Int](./avspeechsynthesisprovidervoice/age.md)
  The age of the voice, in years.
- [var gender: AVSpeechSynthesisVoiceGender](./avspeechsynthesisprovidervoice/gender.md)
  The gender of the voice.
- [enum AVSpeechSynthesisVoiceGender](./avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [var identifier: String](./avspeechsynthesisprovidervoice/identifier.md)
  The unique identifier for the voice.
- [var name: String](./avspeechsynthesisprovidervoice/name.md)
  The localized name of the voice.
- [var primaryLanguages: [String]](./avspeechsynthesisprovidervoice/primarylanguages.md)
  A list of BCP 47 codes that identify the languages the synthesizer uses.
- [var supportedLanguages: [String]](./avspeechsynthesisprovidervoice/supportedlanguages.md)
  A list of BCP 47 codes that identify the languages a voice supports.
- [var version: String](./avspeechsynthesisprovidervoice/version.md)
  The version of the voice.
- [var voiceSize: Int64](./avspeechsynthesisprovidervoice/voicesize.md)
  The size of the voice package on disk, in bytes.
### Updating a voice
- [class func updateSpeechVoices()](./avspeechsynthesisprovidervoice/updatespeechvoices%28%29.md)
  Updates the voices your app provides to the system.
### Initializers
- [init?(coder: NSCoder)](./avspeechsynthesisprovidervoice/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting and setting voices
- [var speechVoices: [AVSpeechSynthesisProviderVoice]](./avspeechsynthesisprovideraudiounit/speechvoices.md)
  A list of voices the audio unit provides to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice)*