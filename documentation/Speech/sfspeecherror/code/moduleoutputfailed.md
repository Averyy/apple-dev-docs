# moduleOutputFailed

**Framework**: Speech  
**Kind**: property

The module’s result task failed.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var moduleOutputFailed: SFSpeechError.Code { get }
```

## See Also

- [static var assetLocaleNotAllocated: SFSpeechError.Code](sfspeecherror/code/assetlocalenotallocated.md)
  The asset locale has not been allocated, but module requires it.
- [static var audioDisordered: SFSpeechError.Code](sfspeecherror/code/audiodisordered.md)
  The audio input time-code overlaps or precedes prior audio input.
- [static var incompatibleAudioFormats: SFSpeechError.Code](sfspeecherror/code/incompatibleaudioformats.md)
  The selected modules do not have an audio format in common.
- [static var noModel: SFSpeechError.Code](sfspeecherror/code/nomodel.md)
  The selected locale/options does not have an appropriate model available or downloadable.
- [static var tooManyAssetLocalesAllocated: SFSpeechError.Code](sfspeecherror/code/toomanyassetlocalesallocated.md)
  The application has allocated too many locales.
- [static var unexpectedAudioFormat: SFSpeechError.Code](sfspeecherror/code/unexpectedaudioformat.md)
  The audio input is in unexpected format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeecherror/code/moduleoutputfailed)*