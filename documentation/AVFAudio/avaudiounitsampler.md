# AVAudioUnitSampler

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioUnitSampler : AVAudioUnitMIDIInstrument
```

## Overview

An `AVAudioUnitSampler` is an [`AVAudioUnit`](./avaudiounit.md) for Apple’s Sampler audio unit.

You configure the sampler by loading instruments from different types of files. These include an `aupreset` file, DLS, or SF2 sound bank; an EXS24 instrument; a single audio file; or an array of audio files.

The output of a `AVAudioUnitSampler` is a single stereo bus.

## Topics

### Configuring the sampler Audio Unit
- [func loadInstrument(at: URL) throws](./avaudiounitsampler/loadinstrument%28at%29.md)
  Configures the sampler with the specified instrument file.
- [func loadAudioFiles(at: [URL]) throws](./avaudiounitsampler/loadaudiofiles%28at%29.md)
  Configures the sampler by loading the specified audio files.
- [func loadSoundBankInstrument(at: URL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws](./avaudiounitsampler/loadsoundbankinstrument%28at,program,bankmsb,banklsb%29.md)
  Loads a specific instrument from the specified soundbank.
### Getting and setting sampler values
- [var globalTuning: Float](./avaudiounitsampler/globaltuning.md)
  An adjustment for the tuning of all the played notes.
- [var overallGain: Float](./avaudiounitsampler/overallgain.md)
  An adjustment for the gain of all the played notes, in decibels.
- [var stereoPan: Float](./avaudiounitsampler/stereopan.md)
  An adjustment for the stereo panning of all the played notes.
- [var masterGain: Float](./avaudiounitsampler/mastergain.md)
  An adjustment for the gain of all the played notes, in decibels.

## Relationships

### Inherits From
- [AVAudioUnitMIDIInstrument](./avaudiounitmidiinstrument.md)
### Conforms To
- [AVAudio3DMixing](./avaudio3dmixing.md)
- [AVAudioMixing](./avaudiomixing.md)
- [AVAudioStereoMixing](./avaudiostereomixing.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### MIDI sequencing and instruments
- [class AVAudioSequencer](./avaudiosequencer.md)
  An object that plays audio from a collection of MIDI events the system organizes into music tracks.
- [typealias AVMIDIEventListBlock](./avmidieventlistblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler)*