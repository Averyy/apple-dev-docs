# NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys for the speech synthesizier information.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
struct SynthesizerInfoKey
```

```c
typedef NSString * NSSpeechSynthesizerInfoKey;
```

#### Discussion

Use constants as keys for the [`synthesizerInfo`](./synthesizerinfo.md) dictionary.

## Topics

### Synthesizer Info Keys
- [static let identifier: NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./synthesizerinfokey/identifier.md)
  The identifier of the speech synthesizer.
- [static let version: NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./synthesizerinfokey/version.md)
  The version of the speech synthesizer.
### Initializers
- [init(rawValue: String)](./synthesizerinfokey/init%28rawvalue%29.md)

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
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.VoiceGender](../voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](../voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](../attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/synthesizerinfokey)*