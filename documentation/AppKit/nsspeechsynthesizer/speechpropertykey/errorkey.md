# NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey

**Framework**: AppKit  
**Kind**: struct

Keys that identify errors that may occur during speech synthesis.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct ErrorKey
```

#### Discussion

Use these keys in the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) dictionary.

## Topics

### Type Properties
- [static let count: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/count.md)
  The number of errors that have occurred in processing the current text string, since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`
- [static let newestCharacterOffset: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/newestcharacteroffset.md)
  The position in the text string of the most recent error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property. An `NSNumber`.
- [static let newestCode: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/newestcode.md)
  The error code of the most recent error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`
- [static let oldestCharacterOffset: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/oldestcharacteroffset.md)
  The position in the text string of the first error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`
- [static let oldestCode: NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](nsspeechsynthesizer/speechpropertykey/errorkey/oldestcode.md)
  The error code of the first error that occurred since the last call to [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md) with the [`errors`](nsspeechsynthesizer/speechpropertykey/errors.md) property.  An `NSNumber`
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/speechpropertykey/errorkey/init(rawvalue:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/errorkey)*