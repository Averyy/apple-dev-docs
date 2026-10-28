# characterMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Get or set the synthesizer’s current text-processing mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let characterMode: NSSpeechSynthesizer.SpeechPropertyKey
```

```c
extern NSSpeechPropertyKey const NSSpeechCharacterModeProperty;
```

## Discussion

An NSString object that specifies whether the channel is currently in text input mode or phoneme input mode.The supported values are listed in [`NSSpeechSynthesizer.SpeechPropertyKey.Mode`](./mode.md).

When the character-processing mode is [`normal`](./mode/normal.md), input characters are spoken as you would expect to hear them. When the mode is [`literal`](./mode/literal.md), each character is spoken literally, so that the word “cat” is spoken “`C–A–T`”.

This property is used with [`setObject(_:forProperty:)`](../setobject%28_,forproperty%29.md) and [`object(forProperty:)`](../object%28forproperty%29.md).

## See Also

### Speech Property Keys
- [static let status: NSSpeechSynthesizer.SpeechPropertyKey](./status.md)
  Get speech-status information for the synthesizer.
- [static let errors: NSSpeechSynthesizer.SpeechPropertyKey](./errors.md)
  Get speech-error information for the synthesizer.
- [static let inputMode: NSSpeechSynthesizer.SpeechPropertyKey](./inputmode.md)
  Get or set the synthesizer’s current text-processing mode.
- [static let numberMode: NSSpeechSynthesizer.SpeechPropertyKey](./numbermode.md)
  Get or set the synthesizer’s current number-processing mode.
- [static let rate: NSSpeechSynthesizer.SpeechPropertyKey](./rate.md)
  Get or set a synthesizer’s speech rate.
- [static let pitchBase: NSSpeechSynthesizer.SpeechPropertyKey](./pitchbase.md)
  Get or set a synthesizer’s baseline speech pitch.
- [static let pitchMod: NSSpeechSynthesizer.SpeechPropertyKey](./pitchmod.md)
  Get or set a synthesizer’s pitch modulation.
- [static let volume: NSSpeechSynthesizer.SpeechPropertyKey](./volume.md)
  Get or set the speech volume for a synthesizer.
- [static let synthesizerInfo: NSSpeechSynthesizer.SpeechPropertyKey](./synthesizerinfo.md)
  Get information about the speech synthesizer being used on the specified synthesizer.
- [static let recentSync: NSSpeechSynthesizer.SpeechPropertyKey](./recentsync.md)
  Get the message code for the most recently encountered synchronization command.
- [static let phonemeSymbols: NSSpeechSynthesizer.SpeechPropertyKey](./phonemesymbols.md)
  Get a list of phoneme symbols and example words defined for the synthesizer.
- [static let currentVoice: NSSpeechSynthesizer.SpeechPropertyKey](./currentvoice.md)
  Set the current voice on the synthesizer to the specified voice.
- [static let commandDelimiter: NSSpeechSynthesizer.SpeechPropertyKey](./commanddelimiter.md)
  Set the embedded speech command delimiter characters to be used for the synthesizer.
- [static let reset: NSSpeechSynthesizer.SpeechPropertyKey](./reset.md)
  Set a synthesizer back to its default state.
- [static let outputToFileURL: NSSpeechSynthesizer.SpeechPropertyKey](./outputtofileurl.md)
  Set the speech output destination to a file or to the computer’s speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/charactermode)*