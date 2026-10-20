# SFSpeechError.Code

**Framework**: Speech  
**Kind**: enum  
**Role**: Enumeration

Error codes that can be thrown under the Speech framework’s error domain.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum SFSpeechErrorCode : NSInteger;
```

## Topics

### Audio input errors
- [static var audioDisordered: SFSpeechError.Code](./code/audiodisordered.md)
  The audio input time-code overlaps or precedes prior audio input.
- [SFSpeechError.Code.audioReadFailed](./code/audioreadfailed.md)
  The audio source could not be read.
### Audio format errors
- [static var incompatibleAudioFormats: SFSpeechError.Code](./code/incompatibleaudioformats.md)
  The selected modules do not have an audio format in common or do not support an audio format.
- [static var unexpectedAudioFormat: SFSpeechError.Code](./code/unexpectedaudioformat.md)
  The audio input is in unexpected format.
### Asset errors
- [static var assetLocaleNotAllocated: SFSpeechError.Code](./code/assetlocalenotallocated.md)
  The asset locale has not been allocated, but module requires it.
- [static var cannotAllocateUnsupportedLocale: SFSpeechError.Code](./code/cannotallocateunsupportedlocale.md)
  The asset locale being requested is not supported by SpeechFramework.
- [static var noModel: SFSpeechError.Code](./code/nomodel.md)
  The selected locale/options does not have an appropriate model available or downloadable.
- [SFSpeechError.Code.timeout](./code/timeout.md)
  The operation timed out.
- [static var tooManyAssetLocalesAllocated: SFSpeechError.Code](./code/toomanyassetlocalesallocated.md)
  The application has allocated too many locales.
### Custom language model errors
- [SFSpeechError.Code.malformedSupplementalModel](./code/malformedsupplementalmodel.md)
  The custom language model file was malformed.
- [SFSpeechError.Code.missingParameter](./code/missingparameter.md)
  A required parameter is missing/nil.
- [SFSpeechError.Code.undefinedTemplateClassName](./code/undefinedtemplateclassname.md)
  The custom language model templates were malformed.
### Other errors
- [static var insufficientResources: SFSpeechError.Code](./code/insufficientresources.md)
  There are not sufficient resources available on-device to process the incoming transcription request.
- [SFSpeechError.Code.internalServiceError](./code/internalserviceerror.md)
  There was an internal error.
- [static var moduleOutputFailed: SFSpeechError.Code](./code/moduleoutputfailed.md)
  The module’s result task failed.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
### Type Properties
- [static var cannotConfigureAudioSystem: SFSpeechError.Code](./code/cannotconfigureaudiosystem.md)
  The audio source could not be configured.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [let SFSpeechErrorDomain: String](../sfspeecherrordomain.md)
- [struct SFSpeechError](../sfspeecherror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeecherror/code)*