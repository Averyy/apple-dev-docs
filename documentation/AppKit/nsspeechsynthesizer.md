# NSSpeechSynthesizer

**Framework**: AppKit  
**Kind**: class

The Cocoa interface to speech synthesis in macOS.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class NSSpeechSynthesizer
```

#### Overview

Speech synthesis, also called text-to-speech (TTS), parses text and converts it into audible speech. It offers a concurrent feedback mode that can be used in concert with or in place of traditional visual and aural notifications. For example, your application can use a speech synthesizer object to “pronounce” the text of important alert dialogs. Synthesized speech has several advantages. It can provide urgent information to users without forcing them to shift attention from their current task. And because speech doesn’t rely on visual elements for meaning, it is a crucial technology for users with vision or attention disabilities.

In addition, synthesized speech can help save system resources. Because sound samples can take up large amounts of room on disk, using text in place of sampled sound is extremely efficient, and so a multimedia application might use an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) object to provide a narration of a QuickTime movie instead of including sampled-sound data on a movie track.

When you create an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) instance using the default initializer (`init`), the class uses the  selected in System Preferences > Speech. Alternatively, you can select a specific voice for an [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) instance by initializing it with [`init(voice:)`](nsspeechsynthesizer/init(voice:).md). To begin synthesis, send either [`startSpeaking(_:)`](nsspeechsynthesizer/startspeaking(_:).md) or [`startSpeaking(_:to:)`](nsspeechsynthesizer/startspeaking(_:to:).md) to the instance. The former generates speech through the system’s default sound output device; the latter saves the generated speech to a file. If you wish to be notified when the current speech concludes, set the [`delegate`](nsspeechsynthesizer/delegate.md) property and implement the delegate method [`speechSynthesizer(_:didFinishSpeaking:)`](nsspeechsynthesizerdelegate/speechsynthesizer(_:didfinishspeaking:).md).

Speech synthesis is just one of the macOS speech technologies. The speech recognizer technology allows applications to “listen to” text spoken in U.S. English; the [`NSSpeechRecognizer`](nsspeechrecognizer.md) class is the Cocoa interface to this technology. Both technologies provide benefits for all users, and are particularly useful to those users who have difficulties seeing the screen or using the mouse and keyboard.

##### Speech Feedback Window

The speech feedback window ([`Figure 1`](nsspeechsynthesizer#1965715.md)) displays the text recognized from the user’s speech and the text from which an `NSSpeechSynthesizer` object synthesizes speech. Using the feedback window makes spoken exchange more natural and helps the user understand the synthesized speech.

![None](https://docs-assets.developer.apple.com/published/41fd24182e5b44a0e32aad125d250bef/media-1965715.jpg)

For example, your application may use an [`NSSpeechRecognizer`](nsspeechrecognizer.md) object to listen for the command “Play some music.” When it recognizes this command, your application might then respond by speaking “Which artist?” using a speech synthesizer.

When `UsesFeedbackWindow` is [`true`](https://developer.apple.com/documentation/swift/true), the speech synthesizer uses the feedback window if its visible, which the user specifies in System Preferences > Speech.

## Topics

### Creating a Speech Synthesizer
- [init?(voice: NSSpeechSynthesizer.VoiceName?)](nsspeechsynthesizer/init(voice:).md)
  Initializes the receiver with a voice.
### Customizing the Speech Synthesizer Behavior
- [var delegate: (any NSSpeechSynthesizerDelegate)?](nsspeechsynthesizer/delegate.md)
  The synthesizer’s delegate.
- [protocol NSSpeechSynthesizerDelegate](nsspeechsynthesizerdelegate.md)
  A set of optional methods implemented by delegates of [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) objects.
### Configuring Speech Synthesizers
- [var usesFeedbackWindow: Bool](nsspeechsynthesizer/usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](nsspeechsynthesizer/voice.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](nsspeechsynthesizer/setvoice(_:).md)
  Sets the receiver’s current voice.
- [var rate: Float](nsspeechsynthesizer/rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](nsspeechsynthesizer/volume.md)
  The synthesizer’s speaking volume.
### Configuring Speech Attributes
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
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](nsspeechsynthesizer/speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](nsspeechsynthesizer/voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](nsspeechsynthesizer/voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).
### Getting Speech Synthesizer Information
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](nsspeechsynthesizer/attributes(forvoice:).md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](nsspeechsynthesizer/voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](nsspeechsynthesizer/voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](nsspeechsynthesizer/attributes(forvoice:).md).
### Getting Speech State
- [class var isAnyApplicationSpeaking: Bool](nsspeechsynthesizer/isanyapplicationspeaking.md)
  A Boolean value indicating whether any application is currently speaking through the sound output device.
### Synthesizing Speech
- [var isSpeaking: Bool](nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](nsspeechsynthesizer/startspeaking(_:).md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](nsspeechsynthesizer/startspeaking(_:to:).md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/pausespeaking(at:).md)
  Pauses synthesis in progress at a given boundary.
- [func continueSpeaking()](nsspeechsynthesizer/continuespeaking.md)
  Resumes synthesis.
- [func stopSpeaking()](nsspeechsynthesizer/stopspeaking.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](nsspeechsynthesizer/stopspeaking(at:).md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](nsspeechsynthesizer/pausespeaking(at:).md) and [`stopSpeaking(at:)`](nsspeechsynthesizer/stopspeaking(at:).md).
### Getting Phonemes
- [func phonemes(from: String) -> String](nsspeechsynthesizer/phonemes(from:).md)
  Provides the phoneme symbols generated by the given text.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSpeechRecognizer](nsspeechrecognizer.md)
  The Cocoa interface to speech recognition in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer)*