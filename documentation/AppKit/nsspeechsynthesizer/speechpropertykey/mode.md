# NSSpeechSynthesizer.SpeechPropertyKey.Mode

**Framework**: AppKit  
**Kind**: struct

Keys for the speaking mode.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct Mode
```

#### Discussion

Use these keys in the [`inputMode`](nsspeechsynthesizer/speechpropertykey/inputmode.md), [`characterMode`](nsspeechsynthesizer/speechpropertykey/charactermode.md), and [`numberMode`](nsspeechsynthesizer/speechpropertykey/numbermode.md) dictionaries.

## Topics

### Type Properties
- [static let literal: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/literal.md)
  Indicates that each digit or character is spoken literally (so that 12 is spoken as “one, two”, or the word “cat” is spoken as “C A T”).
- [static let normal: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/normal.md)
  Indicates that the synthesizer assembles digits into numbers (so that 12 is spoken as “twelve”) and text into words.
- [static let phoneme: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/phoneme.md)
  Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
- [static let text: NSSpeechSynthesizer.SpeechPropertyKey.Mode](nsspeechsynthesizer/speechpropertykey/mode/text.md)
  Indicates that the synthesizer is in text-processing mode.
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/speechpropertykey/mode/init(rawvalue:).md)

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
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](nsspeechsynthesizer/voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](nsspeechsynthesizer/voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/mode)*