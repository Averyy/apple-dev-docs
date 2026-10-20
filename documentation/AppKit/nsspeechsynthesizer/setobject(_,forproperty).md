# setObject(_:forProperty:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies the value of a receiver’s property.

**Availability**:
- macOS 10.5+ - Deprecated in 14.0

## Declaration

```swift
func setObject(_ object: Any?, forProperty property: NSSpeechSynthesizer.SpeechPropertyKey) throws
```

```objc
- (BOOL) setObject:(id) object forProperty:(NSSpeechPropertyKey) property error:(NSError **) outError;
```

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `object`: The property’s new value. The supported properties are listed in `NSSpeechStatusProperty Dictionary Keys`.
- `property`: The property to set.

## See Also

### Configuring Speech Attributes
- [func addSpeechDictionary([NSSpeechSynthesizer.DictionaryKey : Any])](./addspeechdictionary%28_%29.md)
  Registers the given speech dictionary with the receiver.
- [NSSpeechSynthesizer.DictionaryKey](./dictionarykey.md)
  These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](./addspeechdictionary%28_%29.md).
- [func object(forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws -> Any](./object%28forproperty%29.md)
  Provides the value of a receiver’s property.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/setobject(_:forproperty:))*