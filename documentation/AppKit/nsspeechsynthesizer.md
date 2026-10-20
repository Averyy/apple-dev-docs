# NSSpeechSynthesizer

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The Cocoa interface to speech synthesis in macOS.

**Availability**:
- macOS 10.3+ - Deprecated in 14.0

> **Deprecated**: Use AVSpeechSynthesizer in AVFoundation instead

## Declaration

```swift
class NSSpeechSynthesizer
```

```objc
@interface NSSpeechSynthesizer : NSObject
```

#### Overview

Speech synthesis, also called text-to-speech (TTS), parses text and converts it into audible speech. It offers a concurrent feedback mode that can be used in concert with or in place of traditional visual and aural notifications. For example, your application can use a speech synthesizer object to “pronounce” the text of important alert dialogs. Synthesized speech has several advantages. It can provide urgent information to users without forcing them to shift attention from their current task. And because speech doesn’t rely on visual elements for meaning, it is a crucial technology for users with vision or attention disabilities.

In addition, synthesized speech can help save system resources. Because sound samples can take up large amounts of room on disk, using text in place of sampled sound is extremely efficient, and so a multimedia application might use an [`NSSpeechSynthesizer`](./nsspeechsynthesizer.md) object to provide a narration of a QuickTime movie instead of including sampled-sound data on a movie track.

When you create an [`NSSpeechSynthesizer`](./nsspeechsynthesizer.md) instance using the default initializer (`init`), the class uses the **default voice** selected in System Preferences > Speech. Alternatively, you can select a specific voice for an [`NSSpeechSynthesizer`](./nsspeechsynthesizer.md) instance by initializing it with [`init(voice:)`](./nsspeechsynthesizer/init%28voice%29.md). To begin synthesis, send either [`startSpeaking(_:)`](./nsspeechsynthesizer/startspeaking%28_%29.md) or [`startSpeaking(_:to:)`](./nsspeechsynthesizer/startspeaking%28_,to%29.md) to the instance. The former generates speech through the system’s default sound output device; the latter saves the generated speech to a file. If you wish to be notified when the current speech concludes, set the [`delegate`](./nsspeechsynthesizer/delegate.md) property and implement the delegate method [`speechSynthesizer(_:didFinishSpeaking:)`](./nsspeechsynthesizerdelegate/speechsynthesizer%28_,didfinishspeaking%29.md).

Speech synthesis is just one of the macOS speech technologies. The speech recognizer technology allows applications to “listen to” text spoken in U.S. English; the [`NSSpeechRecognizer`](./nsspeechrecognizer.md) class is the Cocoa interface to this technology. Both technologies provide benefits for all users, and are particularly useful to those users who have difficulties seeing the screen or using the mouse and keyboard.

##### Speech Feedback Window

The speech feedback window ([Figure 1](./nsspeechsynthesizer.md#1965715)) displays the text recognized from the user’s speech and the text from which an `NSSpeechSynthesizer` object synthesizes speech. Using the feedback window makes spoken exchange more natural and helps the user understand the synthesized speech.

![A screenshot of the speech feedback window. A microphone-style speech control sits in the center. Above it, a label shows the recognized phrase What Time Is It, and below it, a label shows the synthesized reply It’s 10:54.](https://developer.apple.com/tutorials/images/com.apple.appkit/media-1965715.jpg)

For example, your application may use an [`NSSpeechRecognizer`](./nsspeechrecognizer.md) object to listen for the command “Play some music.” When it recognizes this command, your application might then respond by speaking “Which artist?” using a speech synthesizer.

When `UsesFeedbackWindow` is [`true`](../Swift/true.md), the speech synthesizer uses the feedback window if its visible, which the user specifies in System Preferences > Speech.

## Topics

### Creating a Speech Synthesizer
- [init?(voice: NSSpeechSynthesizer.VoiceName?)](./nsspeechsynthesizer/init%28voice%29.md)
  Initializes the receiver with a voice.
### Customizing the Speech Synthesizer Behavior
- [var delegate: (any NSSpeechSynthesizerDelegate)?](./nsspeechsynthesizer/delegate.md)
  The synthesizer’s delegate.
- [protocol NSSpeechSynthesizerDelegate](./nsspeechsynthesizerdelegate.md)
  A set of optional methods implemented by delegates of [`NSSpeechSynthesizer`](./nsspeechsynthesizer.md) objects.
### Configuring Speech Synthesizers
- [var usesFeedbackWindow: Bool](./nsspeechsynthesizer/usesfeedbackwindow.md)
  Indicates whether the receiver uses the speech feedback window.
- [func voice() -> NSSpeechSynthesizer.VoiceName?](./nsspeechsynthesizer/voice%28%29.md)
  Returns the identifier of the receiver’s current voice.
- [func setVoice(NSSpeechSynthesizer.VoiceName?) -> Bool](./nsspeechsynthesizer/setvoice%28_%29.md)
  Sets the receiver’s current voice.
- [var rate: Float](./nsspeechsynthesizer/rate.md)
  The synthesizer’s speaking rate (words per minute).
- [var volume: Float](./nsspeechsynthesizer/volume.md)
  The synthesizer’s speaking volume.
### Configuring Speech Attributes
- [func addSpeechDictionary([NSSpeechSynthesizer.DictionaryKey : Any])](./nsspeechsynthesizer/addspeechdictionary%28_%29.md)
  Registers the given speech dictionary with the receiver.
- [NSSpeechSynthesizer.DictionaryKey](./nsspeechsynthesizer/dictionarykey.md)
  These constants identify key-value pairs used to add vocabulary to the dictionary using [`addSpeechDictionary(_:)`](./nsspeechsynthesizer/addspeechdictionary%28_%29.md).
- [func object(forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws -> Any](./nsspeechsynthesizer/object%28forproperty%29.md)
  Provides the value of a receiver’s property.
- [func setObject(Any?, forProperty: NSSpeechSynthesizer.SpeechPropertyKey) throws](./nsspeechsynthesizer/setobject%28_,forproperty%29.md)
  Specifies the value of a receiver’s property.
- [NSSpeechSynthesizer.SpeechPropertyKey](./nsspeechsynthesizer/speechpropertykey.md)
  These constants are used with [`setObject(_:forProperty:)`](./nsspeechsynthesizer/setobject%28_,forproperty%29.md) and [`object(forProperty:)`](./nsspeechsynthesizer/object%28forproperty%29.md) to get or set the characteristics of a synthesizer.
- [NSSpeechSynthesizer.SpeechPropertyKey.CommandDelimiterKey](./nsspeechsynthesizer/speechpropertykey/commanddelimiterkey.md)
  Keys for the command delimiters.
- [NSSpeechSynthesizer.SpeechPropertyKey.ErrorKey](./nsspeechsynthesizer/speechpropertykey/errorkey.md)
  Keys that identify errors that may occur during speech synthesis.
- [NSSpeechSynthesizer.SpeechPropertyKey.Mode](./nsspeechsynthesizer/speechpropertykey/mode.md)
  Keys for the speaking mode.
- [NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey](./nsspeechsynthesizer/speechpropertykey/phonemeinfokey.md)
  Keys for the speech phoneme information.
- [NSSpeechSynthesizer.SpeechPropertyKey.StatusKey](./nsspeechsynthesizer/speechpropertykey/statuskey.md)
  Keys for the speech synthesizier status.
- [NSSpeechSynthesizer.SpeechPropertyKey.SynthesizerInfoKey](./nsspeechsynthesizer/speechpropertykey/synthesizerinfokey.md)
  Keys for the speech synthesizier information.
- [NSSpeechSynthesizer.VoiceGender](./nsspeechsynthesizer/voicegender.md)
  The following constants define voice gender attributes, which are the allowable values of the [`gender`](./nsspeechsynthesizer/voiceattributekey/gender.md) key returned by [`attributes(forVoice:)`](./nsspeechsynthesizer/attributes%28forvoice%29.md).
### Getting Speech Synthesizer Information
- [class var availableVoices: [NSSpeechSynthesizer.VoiceName]](./nsspeechsynthesizer/availablevoices.md)
  Provides the identifiers of the voices available on the system.
- [class func attributes(forVoice: NSSpeechSynthesizer.VoiceName) -> [NSSpeechSynthesizer.VoiceAttributeKey : Any]](./nsspeechsynthesizer/attributes%28forvoice%29.md)
  Provides the attribute dictionary of a voice.
- [class var defaultVoice: NSSpeechSynthesizer.VoiceName](./nsspeechsynthesizer/defaultvoice.md)
  Provides the identifier of the default voice.
- [NSSpeechSynthesizer.VoiceName](./nsspeechsynthesizer/voicename.md)
- [NSSpeechSynthesizer.VoiceAttributeKey](./nsspeechsynthesizer/voiceattributekey.md)
  The following constants are keys for the dictionary returned by [`attributes(forVoice:)`](./nsspeechsynthesizer/attributes%28forvoice%29.md).
### Getting Speech State
- [class var isAnyApplicationSpeaking: Bool](./nsspeechsynthesizer/isanyapplicationspeaking.md)
  A Boolean value indicating whether any application is currently speaking through the sound output device.
### Synthesizing Speech
- [var isSpeaking: Bool](./nsspeechsynthesizer/isspeaking.md)
  Indicates whether the receiver is currently generating synthesized speech.
- [func startSpeaking(String) -> Bool](./nsspeechsynthesizer/startspeaking%28_%29.md)
  Begins speaking synthesized text through the system’s default sound output device.
- [func startSpeaking(String, to: URL) -> Bool](./nsspeechsynthesizer/startspeaking%28_,to%29.md)
  Begins synthesizing text into a sound (AIFF) file.
- [func pauseSpeaking(at: NSSpeechSynthesizer.Boundary)](./nsspeechsynthesizer/pausespeaking%28at%29.md)
  Pauses synthesis in progress at a given boundary.
- [func continueSpeaking()](./nsspeechsynthesizer/continuespeaking%28%29.md)
  Resumes synthesis.
- [func stopSpeaking()](./nsspeechsynthesizer/stopspeaking%28%29.md)
  Stops synthesis in progress.
- [func stopSpeaking(at: NSSpeechSynthesizer.Boundary)](./nsspeechsynthesizer/stopspeaking%28at%29.md)
  Stops synthesis in progress at a given boundary.
- [NSSpeechSynthesizer.Boundary](./nsspeechsynthesizer/boundary.md)
  These constants are used to indicate where speech should be stopped and paused. See [`pauseSpeaking(at:)`](./nsspeechsynthesizer/pausespeaking%28at%29.md) and [`stopSpeaking(at:)`](./nsspeechsynthesizer/stopspeaking%28at%29.md).
### Getting Phonemes
- [func phonemes(from: String) -> String](./nsspeechsynthesizer/phonemes%28from%29.md)
  Provides the phoneme symbols generated by the given text.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Speech
- [class NSSpeechRecognizer](./nsspeechrecognizer.md)
  The Cocoa interface to speech recognition in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer)*