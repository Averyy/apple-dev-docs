# NSSpeechSynthesizer.DictionaryKey

**Framework**: AppKit  
**Kind**: struct

These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](nsspeechsynthesizer/addspeechdictionary(_:).md).

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct DictionaryKey
```

## Topics

### Type Properties
- [static let abbreviations: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/abbreviations.md)
  An array of dictionary objects containing the keys [`entrySpelling`](nsspeechsynthesizer/dictionarykey/entryspelling.md) and [`entryPhonemes`](nsspeechsynthesizer/dictionarykey/entryphonemes.md).
- [static let entryPhonemes: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/entryphonemes.md)
  The phonemic representation of an entry. An `NSString`.
- [static let entrySpelling: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/entryspelling.md)
  The spelling of an entry. An `NSString`.
- [static let localeIdentifier: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/localeidentifier.md)
  The canonical locale identifier string describing the dictionary’s locale. A locale is generally composed of three pieces of ordered information: a language code, a region code, and a variant code.  Refer to documentation about [`NSLocale`](https://developer.apple.com/documentation/Foundation/NSLocale) or [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for more information
- [static let modificationDate: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/modificationdate.md)
  A string representation of the dictionary’s last modification date in the international format (YYYY-MM-DD HH:MM:SS ±HHMM). If the same word appears across multiple dictionaries, the one from the dictionary with the most recent date will be used.
- [static let pronunciations: NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey/pronunciations.md)
  An array of dictionary objects containing the keys [`entrySpelling`](nsspeechsynthesizer/dictionarykey/entryspelling.md) and [`entryPhonemes`](nsspeechsynthesizer/dictionarykey/entryphonemes.md).
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/dictionarykey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func addSpeechDictionary([NSSpeechSynthesizer.DictionaryKey : Any])](nsspeechsynthesizer/addspeechdictionary(_:).md)
  Registers the given speech dictionary with the receiver.
- [func object(forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws -> Any](nsspeechsynthesizer/object(forproperty:).md)
  Provides the value of a receiver’s property.
- [func setObject(Any?, forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws](nsspeechsynthesizer/setobject(_:forproperty:).md)
  Specifies the value of a receiver’s property.
- [NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey.md)
  These constants are used with [`setObject(_:forProperty:)`](nsspeechsynthesizer/setobject(_:forproperty:).md) and [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) to get or set the characteristics of a synthesizer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/dictionarykey)*