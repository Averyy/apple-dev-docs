# AVAudioUnitSampler

**Framework**: AVFAudio  
**Kind**: class

An object that you configure with one or more instrument samples, based on Apple’s Sampler audio unit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitSampler
```

#### Overview

An `AVAudioUnitSampler` is an [`AVAudioUnit`](avaudiounit.md) for Apple’s Sampler audio unit.

You configure the sampler by loading instruments from different types of files. These include an `aupreset` file, DLS, or SF2 sound bank; an EXS24 instrument; a single audio file; or an array of audio files.

The output of a `AVAudioUnitSampler` is a single stereo bus.

## Topics

### Configuring the Sampler Audio Unit
- [func loadInstrument(at: URL) throws](avaudiounitsampler/loadinstrument(at:).md)
  Configures the sampler with the specified instrument file.
- [func loadAudioFiles(at: [URL]) throws](avaudiounitsampler/loadaudiofiles(at:).md)
  Configures the sampler by loading the specified audio files.
- [func loadSoundBankInstrument(at: URL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws](avaudiounitsampler/loadsoundbankinstrument(at:program:bankmsb:banklsb:).md)
  Loads a specific instrument from the specified soundbank.
### Getting and Setting Sampler Values
- [var globalTuning: Float](avaudiounitsampler/globaltuning.md)
  An adjustment for the tuning of all the played notes.
- [var overallGain: Float](avaudiounitsampler/overallgain.md)
  An adjustment for the gain of all the played notes, in decibels.
- [var stereoPan: Float](avaudiounitsampler/stereopan.md)
  An adjustment for the stereo panning of all the played notes.
- [var masterGain: Float](avaudiounitsampler/mastergain.md)
  An adjustment for the gain of all the played notes, in decibels.

## Relationships

### Inherits From
- [AVAudioUnitMIDIInstrument](avaudiounitmidiinstrument.md)
### Conforms To
- [AVAudio3DMixing](avaudio3dmixing.md)
- [AVAudioMixing](avaudiomixing.md)
- [AVAudioStereoMixing](avaudiostereomixing.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioSequencer](avaudiosequencer.md)
  An object that plays audio from a collection of MIDI events the system organizes into music tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler)*