# NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys for the speech phoneme information.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
struct PhonemeInfoKey
```

```c
typedef NSString * NSSpeechPhonemeInfoKey;
```

#### Discussion

Use these keys in the [`phonemeSymbols`](./phonemesymbols.md) dictionary.

## Topics

### Phoneme Info Keys
- [static let example: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey/example.md)
  An example word that illustrates the use of the phoneme.
- [static let hiliteEnd: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey/hiliteend.md)
  The character offset into the example word that identifies the location of the end of the phoneme.
- [static let hiliteStart: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey/hilitestart.md)
  The character offset into the example word that identifies the location of the beginning of the phoneme.
- [static let opcode: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey/opcode.md)
  NSNumber
- [static let symbol: NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey/symbol.md)
  The symbol used to represent the phoneme.
### Initializers
- [init(rawValue: String)](./phonemeinfokey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring Speech Attributes
- [func addSpeechDictionary([NSSpeechSynthesizer.DictionaryKey : Any])](../addspeechdictionary%28_%29.md)
  Registers the given speech dictionary with the receiver.
- [NSSpeechSynthesizer.DictionaryKey](../dictionarykey.md)
  These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](../addspeechdictionary%28_%29.md).
- [func object(forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws -> Any](../object%28forproperty%29.md)
  Provides the value of a receiver’s property.
- [func setObject(Any?, forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws](../setobject%28_,forproperty%29.md)
  Specifies the value of a receiver’s property.
- [NSSpeechSynthesizer.SpeechPropertyKey](../speechpropertykey.md)
  These constants are used with [`setObject(_:forProperty:)`](../setobject%28_,forproperty%29.md) and [`object(forProperty:)`](../object%28forproperty%29.md) to get or set the characteristics of a synthesizer.
- [NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](./commanddelimiterkey.md)
  Keys for the command delimiters.
- [NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./errorkey.md)
  Keys that identify errors that may occur during speech synthesis.
- [NSSpeechSynthesizer.SpeechPropertyKey.Mode](./mode.md)
  Keys for the speaking mode.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](../voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](../voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](../attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/phonemeinfokey)*