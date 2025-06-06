# internalFailure

**Framework**: MediaExtension  
**Kind**: property

An error code that indicates the extension encountered an internal operation failure, such as code loading.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static var internalFailure: MEError.Code { get }
```

## See Also

- [static var errorDomain: String](meerror-swift.struct/errordomain-6dfr0.md)
  The domain of the error.
- [static var allocationFailure: MEError.Code](meerror-swift.struct/allocationfailure.md)
  An error code that indicates the extension can’t allocate memory.
- [static var endOfStream: MEError.Code](meerror-swift.struct/endofstream.md)
  An error code that indicates the extension reached the end of the source file.
- [static var invalidParameter: MEError.Code](meerror-swift.struct/invalidparameter.md)
  An error code that indicates the extension received an invalid parameter.
- [static var locationNotAvailable: MEError.Code](meerror-swift.struct/locationnotavailable.md)
  An error code that indicates a specific sample isn’t contiguous, spans more than one file, or is for some other reason unsuitable to read directly from a file.
- [static var noSamples: MEError.Code](meerror-swift.struct/nosamples.md)
  An error code that indicates there are no samples in the track or a request to load a sample buffer fails.
- [static var noSuchEdit: MEError.Code](meerror-swift.struct/nosuchedit.md)
  An error code that indicates the plug-in track reader received a request to return an edit that’s out of range.
- [static var parsingFailure: MEError.Code](meerror-swift.struct/parsingfailure.md)
  An error code that indicates the extension encountered an error while parsing the media.
- [static var permissionDenied: MEError.Code](meerror-swift.struct/permissiondenied.md)
  An error code that indicates the extension received a request to perform an invalid operation on a byte source.
- [static var propertyNotSupported: MEError.Code](meerror-swift.struct/propertynotsupported.md)
  An error code that indicates the extension encountered a property it doesn’t support reading and writing to.
- [static var referenceMissing: MEError.Code](meerror-swift.struct/referencemissing.md)
  An error code that indicates the decoder received a request to decode a sample without decoding the required reference frame dependencies first.
- [static var unsupportedFeature: MEError.Code](meerror-swift.struct/unsupportedfeature.md)
  An error code that indicates the extension doesn’t support an aspect of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meerror-swift.struct/internalfailure)*