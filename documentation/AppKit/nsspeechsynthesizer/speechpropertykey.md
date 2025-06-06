# NSSpeechSynthesizer.SpeechPropertyKey

**Framework**: AppKit  
**Kind**: struct

These constants are used with [`setObject(_:forProperty:)`](nsspeechsynthesizer/setobject(_:forproperty:).md) and [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) to get or set the characteristics of a synthesizer.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct SpeechPropertyKey
```

## Topics

### Speech Property Keys
- [static let status: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/status.md)
  Get speech-status information for the synthesizer.
- [static let errors: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/errors.md)
  Get speech-error information for the synthesizer.
- [static let inputMode: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/inputmode.md)
  Get or set the synthesizer’s current text-processing mode.
- [static let characterMode: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/charactermode.md)
  Get or set the synthesizer’s current text-processing mode.
- [static let numberMode: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/numbermode.md)
  Get or set the synthesizer’s current number-processing mode.
- [static let rate: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/rate.md)
  Get or set a synthesizer’s speech rate.
- [static let pitchBase: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/pitchbase.md)
  Get or set a synthesizer’s baseline speech pitch.
- [static let pitchMod: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/pitchmod.md)
  Get or set a synthesizer’s pitch modulation.
- [static let volume: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/volume.md)
  Get or set the speech volume for a synthesizer.
- [static let synthesizerInfo: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfo.md)
  Get information about the speech synthesizer being used on the specified synthesizer.
- [static let recentSync: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/recentsync.md)
  Get the message code for the most recently encountered synchronization command.
- [static let phonemeSymbols: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/phonemesymbols.md)
  Get a list of phoneme symbols and example words defined for the synthesizer.
- [static let currentVoice: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/currentvoice.md)
  Set the current voice on the synthesizer to the specified voice.
- [static let commandDelimiter: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/commanddelimiter.md)
  Set the embedded speech command delimiter characters to be used for the synthesizer.
- [static let reset: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/reset.md)
  Set a synthesizer back to its default state.
- [static let outputToFileURL: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/outputtofileurl.md)
  Set the speech output destination to a file or to the computer’s speakers.
### Type Aliases
- [NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](nsspeechsynthesizer/speechpropertykey/commanddelimiterkey.md)
  Keys for the command delimiters.
- [NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey.md)
  Keys that identify errors that may occur during speech synthesis.
- [NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode.md)
  Keys for the speaking mode.
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/speechpropertykey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func addSpeechDictionary([NSSpeechSynthesizer.DictionaryKey : Any])](nsspeechsynthesizer/addspeechdictionary(_:).md)
  Registers the given speech dictionary with the receiver.
- [NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey.md)
  These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](nsspeechsynthesizer/addspeechdictionary(_:).md).
- [func object(forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws -> Any](nsspeechsynthesizer/object(forproperty:).md)
  Provides the value of a receiver’s property.
- [func setObject(Any?, forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws](nsspeechsynthesizer/setobject(_:forproperty:).md)
  Specifies the value of a receiver’s property.
- [NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](nsspeechsynthesizer/speechpropertykey/commanddelimiterkey.md)
  Keys for the command delimiters.
- [NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey.md)
  Keys that identify errors that may occur during speech synthesis.
- [NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode.md)
  Keys for the speaking mode.
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](nsspeechsynthesizer/voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](nsspeechsynthesizer/voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey)*