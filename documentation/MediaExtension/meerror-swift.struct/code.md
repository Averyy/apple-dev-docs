# MEError.Code

**Framework**: MediaExtension  
**Kind**: enum  
**Role**: Enumeration

An enumeration that models media extension error codes.

**Availability**:
- macOS 14.0+

## Declaration

```swift
enum Code
```

```c
enum MEError : NSInteger;
```

## Topics

### Error codes
- [MEError.Code.allocationFailure](./code/allocationfailure.md)
  An error code that indicates the extension can’t allocate memory.
- [MEError.Code.endOfStream](./code/endofstream.md)
  An error code that indicates the extension reached the end of the source file.
- [MEError.Code.internalFailure](./code/internalfailure.md)
  An error code that indicates the extension encountered an internal operation failure, such as code loading.
- [MEError.Code.invalidParameter](./code/invalidparameter.md)
  An error code that indicates the extension received an invalid parameter.
- [MEError.Code.locationNotAvailable](./code/locationnotavailable.md)
  An error code that indicates specific sample isn’t contiguous, spans more than one file, or is for some other reason unsuitable for reading directly from a file.
- [MEError.Code.noSamples](./code/nosamples.md)
  An error code that indicates there are no samples in the track or a request to load a sample buffer fails.
- [MEError.Code.noSuchEdit](./code/nosuchedit.md)
  An error code that indicates the plug-in track reader received a request to return an edit that’s out of range.
- [MEError.Code.parsingFailure](./code/parsingfailure.md)
  An error code that indicates the extension encountered an error while parsing the media.
- [MEError.Code.permissionDenied](./code/permissiondenied.md)
  An error code that indicates the extension received a request to perform an invalid operation on a byte source.
- [MEError.Code.propertyNotSupported](./code/propertynotsupported.md)
  An error code that indicates the extension encountered a property it doesn’t support reading and writing to.
- [MEError.Code.referenceMissing](./code/referencemissing.md)
  An error code that indicates the decoder received a request to decode a sample without decoding the required reference frame dependencies first.
- [MEError.Code.unsupportedFeature](./code/unsupportedfeature.md)
  An error code that indicates the extension doesn’t support an aspect of the media.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

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
- [let MediaExtensionErrorDomain: String](../mediaextensionerrordomain.md)
  The domain of the error.
- [struct MEError](../meerror-swift.struct.md)
  A MediaExtension framework error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meerror-swift.struct/code)*