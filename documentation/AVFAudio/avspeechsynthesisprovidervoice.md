# AVSpeechSynthesisProviderVoice

**Framework**: AVFAudio  
**Kind**: class

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

#### Overview

This is a voice that an [`AVSpeechSynthesisProviderAudioUnit`](avspeechsynthesisprovideraudiounit.md) provides to the system, distinct from [`AVSpeechSynthesisVoice`](avspeechsynthesisvoice.md). Use [`speechVoices`](avspeechsynthesisprovideraudiounit/speechvoices.md) to access the underlying [`AVSpeechSynthesisVoice`](avspeechsynthesisvoice.md) in the voice quality [`AVSpeechSynthesisVoiceQuality.enhanced`](avspeechsynthesisvoicequality/enhanced.md).

## Topics

### Creating a voice
- [init(name: String, identifier: String, primaryLanguages: [String], supportedLanguages: [String])](avspeechsynthesisprovidervoice/init(name:identifier:primarylanguages:supportedlanguages:).md)
  Creates a voice with a name, an identifier, and language information.
### Inspecting a voice
- [var age: Int](avspeechsynthesisprovidervoice/age.md)
  The age of the voice, in years.
- [var gender: AVSpeechSynthesisVoiceGender](avspeechsynthesisprovidervoice/gender.md)
  The gender of the voice.
- [enum AVSpeechSynthesisVoiceGender](avspeechsynthesisvoicegender.md)
  The gender for a voice.
- [var identifier: String](avspeechsynthesisprovidervoice/identifier.md)
  The unique identifier for the voice.
- [var name: String](avspeechsynthesisprovidervoice/name.md)
  The localized name of the voice.
- [var primaryLanguages: [String]](avspeechsynthesisprovidervoice/primarylanguages.md)
  A list of BCP 47 codes that identify the languages the synthesizer uses.
- [var supportedLanguages: [String]](avspeechsynthesisprovidervoice/supportedlanguages.md)
  A list of BCP 47 codes that identify the languages a voice supports.
- [var version: String](avspeechsynthesisprovidervoice/version.md)
  The version of the voice.
- [var voiceSize: Int64](avspeechsynthesisprovidervoice/voicesize.md)
  The size of the voice package on disk, in bytes.
### Updating a voice
- [class func updateSpeechVoices()](avspeechsynthesisprovidervoice/updatespeechvoices.md)
  Updates the voices your app provides to the system.

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var speechVoices: [AVSpeechSynthesisProviderVoice]](avspeechsynthesisprovideraudiounit/speechvoices.md)
  A list of voices the audio unit provides to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice)*