# NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey

**Framework**: AppKit  
**Kind**: struct

Keys for the speech phoneme information.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct PhonemeInfoKey
```

#### Discussion

Use these keys in the [`phonemeSymbols`](nsspeechsynthesizer/speechpropertykey/phonemesymbols.md) dictionary.

## Topics

### Phoneme Info Keys
- [static let example: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey/example.md)
  An example word that illustrates the use of the phoneme.
- [static let hiliteEnd: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey/hiliteend.md)
  The character offset into the example word that identifies the location of the end of the phoneme.
- [static let hiliteStart: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey/hilitestart.md)
  The character offset into the example word that identifies the location of the beginning of the phoneme.
- [static let opcode: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey/opcode.md)
  NSNumber
- [static let symbol: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey/symbol.md)
  The symbol used to represent the phoneme.
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/speechpropertykey/phonemeinfokey/init(rawvalue:).md)

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
- [NSSpeechSynthesizer.DictionaryKey](nsspeechsynthesizer/dictionarykey.md)
  These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](nsspeechsynthesizer/addspeechdictionary(_:).md).
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
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](nsspeechsynthesizer/voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](nsspeechsynthesizer/voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/phonemeinfokey)*