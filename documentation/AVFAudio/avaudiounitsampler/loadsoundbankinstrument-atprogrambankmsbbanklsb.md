# loadSoundBankInstrument(at:program:bankMSB:bankLSB:)

**Framework**: AVFAudio  
**Kind**: method

Loads a specific instrument from the specified soundbank.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func loadSoundBankInstrument(at bankURL: URL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws
```

#### Discussion

> ❗ **Important**:  This method reads from the file and allocates memory. Don’t call it on a real-time thread.

 This method reads from the file and allocates memory. Don’t call it on a real-time thread.

## Parameters

- `bankURL`: The URL for a soundbank file, either a DLS bank ( ) or a SoundFont bank ( ).
- `program`: The program number for the instrument to load.
- `bankMSB`: The most significant bit for the bank number for the instrument to load. This is usually   for melodic instruments and   for percussion instruments.
- `bankLSB`: The least significant bit for the bank number for the instrument to load. This is often   and represents the bank variation.

## See Also

- [func loadInstrument(at: URL) throws](avaudiounitsampler/loadinstrument(at:).md)
  Configures the sampler with the specified instrument file.
- [func loadAudioFiles(at: [URL]) throws](avaudiounitsampler/loadaudiofiles(at:).md)
  Configures the sampler by loading the specified audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/loadsoundbankinstrument(at:program:bankmsb:banklsb:))*