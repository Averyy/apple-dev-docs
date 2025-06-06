# rate

**Framework**: AppKit  
**Kind**: property

Get or set a synthesizer’s speech rate.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let rate: NSSpeechSynthesizer.SpeechPropertyKey
```

#### Discussion

An [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that specifies the synthesizer’s speaking rate. The range of supported rates is not predefined by the [`NSSpeechSynthesizer`](nsspeechsynthesizer.md) class; each speech synthesizer provides its own range of speech rates. Average human speech occurs at a rate of 180 to 220 words per minute.

This property is used with [`setObject(_:forProperty:)`](nsspeechsynthesizer/setobject(_:forproperty:).md) and [`object(forProperty:)`](nsspeechsynthesizer/object(forproperty:).md).

## See Also

- [static let status: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/status.md)
  Get speech-status information for the synthesizer.
- [static let errors: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/errors.md)
  Get speech-error information for the synthesizer.
- [static let inputMode: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/inputmode.md)
  Get or set the synthesizer’s current text-processing mode.
- [static let characterMode: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/charactermode.md)
  Get or set the synthesizer’s current text-processing mode.
- [static let numberMode: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/numbermode.md)
  Get or set the synthesizer’s current number-processing mode.
- [static let pitchBase: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/pitchbase.md)
  Get or set a synthesizer’s baseline speech pitch.
- [static let pitchMod: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/pitchmod.md)
  Get or set a synthesizer’s pitch modulation.
- [static let volume: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/volume.md)
  Get or set the speech volume for a synthesizer.
- [static let synthesizerInfo: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/synthesizerinfo.md)
  Get information about the speech synthesizer being used on the specified synthesizer.
- [static let recentSync: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/recentsync.md)
  Get the message code for the most recently encountered synchronization command.
- [static let phonemeSymbols: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/phonemesymbols.md)
  Get a list of phoneme symbols and example words defined for the synthesizer.
- [static let currentVoice: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/currentvoice.md)
  Set the current voice on the synthesizer to the specified voice.
- [static let commandDelimiter: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/commanddelimiter.md)
  Set the embedded speech command delimiter characters to be used for the synthesizer.
- [static let reset: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/reset.md)
  Set a synthesizer back to its default state.
- [static let outputToFileURL: NSSpeechSynthesizer.SpeechPropertyKey](nsspeechsynthesizer/speechpropertykey/outputtofileurl.md)
  Set the speech output destination to a file or to the computer’s speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/rate)*