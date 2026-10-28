# addSpeechDictionary(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers the given speech dictionary with the receiver.

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
func addSpeechDictionary(_ speechDictionary: [NSSpeechSynthesizer.DictionaryKey : Any])
```

```objc
- (void) addSpeechDictionary:(NSDictionary<NSString *,id> *) speechDictionary;
```

## Discussion

See the discussion of [`UseSpeechDictionary(_:_:)`](../../applicationservices/api-1463688-usespeechdictionary.md) in [Speech Synthesis Manager](../../applicationservices/speech_synthesis_manager.md) for more information.

## Parameters

- `speechDictionary`: Speech dictionary to add to the receiver’s dictionaries. The key-value pairs are listed in `Speech Dictionary Properties Keys`.

## See Also

### Configuring Speech Attributes
- [NSSpeechSynthesizer.DictionaryKey](./dictionarykey.md)
  These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](./addspeechdictionary%28_%29.md).
- [func object(forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws -> Any](./object%28forproperty%29.md)
  Provides the value of a receiver’s property.
- [func setObject(Any?, forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws](./setobject%28_,forproperty%29.md)
  Specifies the value of a receiver’s property.
- [NSSpeechSynthesizer.SpeechPropertyKey](./speechpropertykey.md)
  These constants are used with [`setObject(_:forProperty:)`](./setobject%28_,forproperty%29.md) and [`object(forProperty:)`](./object%28forproperty%29.md) to get or set the characteristics of a synthesizer.
- [NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](./speechpropertykey/commanddelimiterkey.md)
  Keys for the command delimiters.
- [NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./speechpropertykey/errorkey.md)
  Keys that identify errors that may occur during speech synthesis.
- [NSSpeechSynthesizer.SpeechPropertyKey.Mode](./speechpropertykey/mode.md)
  Keys for the speaking mode.
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./speechpropertykey/phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](./voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](./voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](./attributes%28forvoice%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/addspeechdictionary(_:))*