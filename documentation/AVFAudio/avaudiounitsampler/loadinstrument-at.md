# loadInstrument(at:)

**Framework**: AVFAudio  
**Kind**: method

Configures the sampler with the specified instrument file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func loadInstrument(at instrumentURL: URL) throws
```

#### Discussion

The instrument can be one of the following types: Logic or GarageBand `EXS24`, the sampler’s native `aupreset` file, or an audio file, such as `caf`, `aiff`, `wav`, or `mp3`.

For a single audio file, the framework loads it into a new default instrument and uses any information in the audio file, such as the root key and key range, for its placement in the instrument.

## Parameters

- `instrumentURL`: The URL of the file that contains the instrument.

## See Also

- [func loadAudioFiles(at: [URL]) throws](avaudiounitsampler/loadaudiofiles(at:).md)
  Configures the sampler by loading the specified audio files.
- [func loadSoundBankInstrument(at: URL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws](avaudiounitsampler/loadsoundbankinstrument(at:program:bankmsb:banklsb:).md)
  Loads a specific instrument from the specified soundbank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/loadinstrument(at:))*