# NSSpeechSynthesizer.SpeechPropertyKey.StatusKey

**Framework**: AppKit  
**Kind**: struct

Keys for the speech synthesizier status.

**Availability**:
- macOS 10.3+

## Declaration

```swift
struct StatusKey
```

#### Discussion

Use these keys in the [`status`](nsspeechsynthesizer/speechpropertykey/status.md) dictionary.

## Topics

### Status Keys
- [static let numberOfCharactersLeft: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/numberofcharactersleft.md)
  The number of characters left in the input string of text.
- [static let outputBusy: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/outputbusy.md)
  Indicates whether the synthesizer is currently producing speech.
- [static let outputPaused: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/outputpaused.md)
  Indicates whether speech output in the synthesizer has been paused by sending the message [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md).
- [static let phonemeCode: NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey/phonemecode.md)
  Indicates that the synthesizer is in phoneme-processing mode. When in phoneme-processing mode, a text buffer is interpreted to be a series of characters representing various phonemes and prosodic controls.
### Initializers
- [init(rawValue: String)](nsspeechsynthesizer/speechpropertykey/statuskey/init(rawvalue:).md)

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
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](nsspeechsynthesizer/speechpropertykey/phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](nsspeechsynthesizer/voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](nsspeechsynthesizer/voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/statuskey)*