# pitchBase

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Get or set a synthesizer’s baseline speech pitch.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let pitchBase: NSSpeechSynthesizer.SpeechPropertyKey
```

```c
extern NSSpeechPropertyKey const NSSpeechPitchBaseProperty;
```

## Discussion

An [`NSNumber`](../../../Foundation/nsnumber.md) object that specifies the baseline speech pitch. Typical voice frequencies range from around 90 hertz for a low-pitched voice to perhaps 300 hertz for a high-pitched voice. These frequencies correspond to approximate pitch values in the ranges of 30.000 to 40.000 and 55.000 to 65.000, respectively.

This property is used with [`setObject(_:forProperty:)`](../setobject%28_,forproperty%29.md) and [`object(forProperty:)`](../object%28forproperty%29.md).

> **Note**:  The change in speech pitch may not be noticeable until the next sentence or paragraph is spoken.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspeechsynthesizer/speechpropertykey/pitchbase)*