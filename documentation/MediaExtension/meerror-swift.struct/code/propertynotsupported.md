# MEError.Code.propertyNotSupported

**Framework**: MediaExtension  
**Kind**: case

An error code that indicates the extension encountered a property it doesn’t support reading and writing to.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case propertyNotSupported
```

## See Also

- [MEError.Code.allocationFailure](meerror-swift.struct/code/allocationfailure.md)
  An error code that indicates the extension can’t allocate memory.
- [MEError.Code.endOfStream](meerror-swift.struct/code/endofstream.md)
  An error code that indicates the extension reached the end of the source file.
- [MEError.Code.internalFailure](meerror-swift.struct/code/internalfailure.md)
  An error code that indicates the extension encountered an internal operation failure, such as code loading.
- [MEError.Code.invalidParameter](meerror-swift.struct/code/invalidparameter.md)
  An error code that indicates the extension received an invalid parameter.
- [MEError.Code.locationNotAvailable](meerror-swift.struct/code/locationnotavailable.md)
  An error code that indicates specific sample isn’t contiguous, spans more than one file, or is for some other reason unsuitable for reading directly from a file.
- [MEError.Code.noSamples](meerror-swift.struct/code/nosamples.md)
  An error code that indicates there are no samples in the track or a request to load a sample buffer fails.
- [MEError.Code.noSuchEdit](meerror-swift.struct/code/nosuchedit.md)
  An error code that indicates the plug-in track reader received a request to return an edit that’s out of range.
- [MEError.Code.parsingFailure](meerror-swift.struct/code/parsingfailure.md)
  An error code that indicates the extension encountered an error while parsing the media.
- [MEError.Code.permissionDenied](meerror-swift.struct/code/permissiondenied.md)
  An error code that indicates the extension received a request to perform an invalid operation on a byte source.
- [MEError.Code.referenceMissing](meerror-swift.struct/code/referencemissing.md)
  An error code that indicates the decoder received a request to decode a sample without decoding the required reference frame dependencies first.
- [MEError.Code.unsupportedFeature](meerror-swift.struct/code/unsupportedfeature.md)
  An error code that indicates the extension doesn’t support an aspect of the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/meerror-swift.struct/code/propertynotsupported)*