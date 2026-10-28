# NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys for the command delimiters.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
struct CommandDelimiterKey
```

```c
typedef NSString * NSSpeechCommandDelimiterKey;
```

## Discussion

Use these keys in the [`commandDelimiter`](./commanddelimiter.md) dictionary.

## Topics

### Delimiter Keys
- [static let prefix: NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](./commanddelimiterkey/prefix.md)
  The command delimiter string that prefixes a command, by default, this is `[[`.
- [static let suffix: NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](./commanddelimiterkey/suffix.md)
  The command delimiter string that suffixes a command,by default, this is `]]`.
### Initializers
- [init(rawValue: String)](./commanddelimiterkey/init%28rawvalue%29.md)

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
- [NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./errorkey.md)
  Keys that identify errors that may occur during speech synthesis.
- [NSSpeechSynthesizer.SpeechPropertyKey.Mode](./mode.md)
  Keys for the speaking mode.
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](../voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](../voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](../attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/commanddelimiterkey)*