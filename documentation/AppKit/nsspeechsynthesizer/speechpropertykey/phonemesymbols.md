# phonemeSymbols

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Get a list of phoneme symbols and example words defined for the synthesizer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let phonemeSymbols: NSSpeechSynthesizer.SpeechPropertyKey
```

```c
extern NSSpeechPropertyKey const NSSpeechPhonemeSymbolsProperty;
```

## Discussion

A dictionary object that contains the phoneme symbols and example words defined for the current synthesizer.

Your application might use this information to show the user what symbols to use when entering phonemic text directly. See [`NSSpeechSynthesizer.SpeechPropertyKey.PhonemeInfoKey`](./phonemeinfokey.md) for a description of the keys present in the dictionary.

This property works with [`setObject(_:forProperty:)`](../setobject%28_,forproperty%29.md).

## See Also

### Speech Property Keys
- [static let status: NSSpeechSynthesizer.SpeechPropertyKey](./status.md)
  Get speech-status information for the synthesizer.
- [static let errors: NSSpeechSynthesizer.SpeechPropertyKey](./errors.md)
  Get speech-error information for the synthesizer.
- [static let inputMode: NSSpeechSynthesizer.SpeechPropertyKey](./inputmode.md)
  Get or set the synthesizer’s current text-processing mode.
- [static let characterMode: NSSpeechSynthesizer.SpeechPropertyKey](./charactermode.md)
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
- [static let currentVoice: NSSpeechSynthesizer.SpeechPropertyKey](./currentvoice.md)
  Set the current voice on the synthesizer to the specified voice.
- [static let commandDelimiter: NSSpeechSynthesizer.SpeechPropertyKey](./commanddelimiter.md)
  Set the embedded speech command delimiter characters to be used for the synthesizer.
- [static let reset: NSSpeechSynthesizer.SpeechPropertyKey](./reset.md)
  Set a synthesizer back to its default state.
- [static let outputToFileURL: NSSpeechSynthesizer.SpeechPropertyKey](./outputtofileurl.md)
  Set the speech output destination to a file or to the computer’s speakers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/phonemesymbols)*