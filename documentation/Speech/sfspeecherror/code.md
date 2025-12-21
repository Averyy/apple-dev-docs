# SFSpeechError.Code

**Framework**: Speech  
**Kind**: enum

Error codes that can be thrown under the Speech framework’s error domain.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Audio input errors
- [static var audioDisordered: SFSpeechError.Code](sfspeecherror/code/audiodisordered.md)
  The audio input time-code overlaps or precedes prior audio input.
- [SFSpeechError.Code.audioReadFailed](sfspeecherror/code/audioreadfailed.md)
  The audio file could not be read.
### Audio format errors
- [static var incompatibleAudioFormats: SFSpeechError.Code](sfspeecherror/code/incompatibleaudioformats.md)
  The selected modules do not have an audio format in common.
- [static var unexpectedAudioFormat: SFSpeechError.Code](sfspeecherror/code/unexpectedaudioformat.md)
  The audio input is in unexpected format.
### Asset errors
- [static var assetLocaleNotAllocated: SFSpeechError.Code](sfspeecherror/code/assetlocalenotallocated.md)
  The asset locale has not been allocated, but module requires it.
- [static var cannotAllocateUnsupportedLocale: SFSpeechError.Code](sfspeecherror/code/cannotallocateunsupportedlocale.md)
  The asset locale being requested is not supported by SpeechFramework.
- [static var noModel: SFSpeechError.Code](sfspeecherror/code/nomodel.md)
  The selected locale/options does not have an appropriate model available or downloadable.
- [SFSpeechError.Code.timeout](sfspeecherror/code/timeout.md)
  The operation timed out.
- [static var tooManyAssetLocalesAllocated: SFSpeechError.Code](sfspeecherror/code/toomanyassetlocalesallocated.md)
  The application has allocated too many locales.
### Custom language model errors
- [SFSpeechError.Code.malformedSupplementalModel](sfspeecherror/code/malformedsupplementalmodel.md)
  The custom language model file was malformed.
- [SFSpeechError.Code.missingParameter](sfspeecherror/code/missingparameter.md)
  A required parameter is missing/nil.
- [SFSpeechError.Code.undefinedTemplateClassName](sfspeecherror/code/undefinedtemplateclassname.md)
  The custom language model templates were malformed.
### Other errors
- [static var insufficientResources: SFSpeechError.Code](sfspeecherror/code/insufficientresources.md)
  There are not sufficient resources available on-device to process the incoming transcription request.
- [SFSpeechError.Code.internalServiceError](sfspeecherror/code/internalserviceerror.md)
  There was an internal error.
- [static var moduleOutputFailed: SFSpeechError.Code](sfspeecherror/code/moduleoutputfailed.md)
  The module’s result task failed.
### Initializers
- [init?(rawValue: Int)](sfspeecherror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let SFSpeechErrorDomain: String](sfspeecherrordomain.md)
- [struct SFSpeechError](sfspeecherror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeecherror/code)*