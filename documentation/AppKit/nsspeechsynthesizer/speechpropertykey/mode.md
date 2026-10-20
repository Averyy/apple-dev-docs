# NSSpeechSynthesizer.SpeechPropertyKey.Mode

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys for the speaking mode.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
struct Mode
```

```c
typedef NSString * NSSpeechMode;
```

#### Discussion

Use these keys in the [`inputMode`](./inputmode.md), [`characterMode`](./charactermode.md), and [`numberMode`](./numbermode.md) dictionaries.

## Topics

### Type Properties
- [static let literal: NSSpeechSynthesizer.SpeechPropertyKey.Mode](./mode/literal.md)
  Indicates that each digit or character is spoken literally (so that 12 is spoken as “one, two”, or the word “cat” is spoken as “C A T”).
- [static let normal: NSSpeechSynthesizer.SpeechPropertyKey.Mode](./mode/normal.md)
  Indicates that the synthesizer assembles digits into numbers (so that 12 is spoken as “twelve”) and text into words.
- [static let phoneme: NSSpeechSynthesizer.SpeechPropertyKey.Mode](./mode/phoneme.md)
  Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
- [static let text: NSSpeechSynthesizer.SpeechPropertyKey.Mode](./mode/text.md)
  Indicates that the synthesizer is in text-processing mode.
### Initializers
- [init(rawValue: String)](./mode/init%28rawvalue%29.md)

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
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](../voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](../voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](../attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/mode)*