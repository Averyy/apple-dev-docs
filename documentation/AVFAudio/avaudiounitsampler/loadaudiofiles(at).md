# loadAudioFiles(at:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Configures the sampler by loading the specified audio files.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func loadAudioFiles(at audioFiles: [URL]) throws
```

```objc
- (BOOL) loadAudioFilesAtURLs:(NSArray<NSURL *> *) audioFiles error:(NSError **) outError;
```

#### Discussion

The framework loads the audio files into a new instrument with each audio file in its own sampler zone. The framework uses any information in the audio file for its placement in the instrument. For example, the root key and key range.

## Parameters

- `audioFiles`: An array of audio file URLs to load.

## See Also

### Configuring the sampler Audio Unit
- [func loadInstrument(at: URL) throws](./loadinstrument%28at%29.md)
  Configures the sampler with the specified instrument file.
- [func loadSoundBankInstrument(at: URL, program: UInt8, bankMSB: UInt8, bankLSB: UInt8) throws](./loadsoundbankinstrument%28at,program,bankmsb,banklsb%29.md)
  Loads a specific instrument from the specified soundbank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitsampler/loadaudiofiles(at:))*