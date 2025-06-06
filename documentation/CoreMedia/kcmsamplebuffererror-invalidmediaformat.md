# kCMSampleBufferError_InvalidMediaFormat

**Framework**: Core Media  
**Kind**: var

An error code that indicates the media format doesn’t match the sample buffer’s format description.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCMSampleBufferError_InvalidMediaFormat: OSStatus { get }
```

## See Also

- [var kCMSampleBufferError_AllocationFailed: OSStatus](kcmsamplebuffererror_allocationfailed.md)
  An error code that indicates the system failed to allocate memory.
- [var kCMSampleBufferError_AlreadyHasDataBuffer: OSStatus](kcmsamplebuffererror_alreadyhasdatabuffer.md)
  An error code that indicates an attempt to set data on a sample buffer failed because that buffer already contains media data.
- [var kCMSampleBufferError_ArrayTooSmall: OSStatus](kcmsamplebuffererror_arraytoosmall.md)
  An error code that indicates the output array isn’t large enough to hold the requested array.
- [var kCMSampleBufferError_BufferHasNoSampleSizes: OSStatus](kcmsamplebuffererror_bufferhasnosamplesizes.md)
  An error code that indicates a request for sample sizes on a buffer failed because the buffer doesn’t provide that information.
- [var kCMSampleBufferError_BufferHasNoSampleTimingInfo: OSStatus](kcmsamplebuffererror_bufferhasnosampletiminginfo.md)
  An error code that indicates a request for sample timing on a buffer failed because the buffer doesn’t contain that information.
- [var kCMSampleBufferError_BufferNotReady: OSStatus](kcmsamplebuffererror_buffernotready.md)
  An error code that indicates the system can’t make the buffer’s data ready for use.
- [var kCMSampleBufferError_CannotSubdivide: OSStatus](kcmsamplebuffererror_cannotsubdivide.md)
  An error code that indicates a sample buffer doesn’t contain sample sizes.
- [var kCMSampleBufferError_DataCanceled: OSStatus](kcmsamplebuffererror_datacanceled.md)
  An error code that indicates a sample buffer canceled its data-loading operation.
- [var kCMSampleBufferError_DataFailed: OSStatus](kcmsamplebuffererror_datafailed.md)
  An error code that indicates a sample buffer failed to load its data.
- [var kCMSampleBufferError_InvalidEntryCount: OSStatus](kcmsamplebuffererror_invalidentrycount.md)
  An error code that indicates a timing or size value isn’t within the allowed range.
- [var kCMSampleBufferError_InvalidMediaTypeForOperation: OSStatus](kcmsamplebuffererror_invalidmediatypeforoperation.md)
  An error code that indicates the media type that the format description defines isn’t a value for the requested operation.
- [var kCMSampleBufferError_InvalidSampleData: OSStatus](kcmsamplebuffererror_invalidsampledata.md)
  An error code that indicates the sample buffer contains bad data.
- [var kCMSampleBufferError_Invalidated: OSStatus](kcmsamplebuffererror_invalidated.md)
  An error code that indicates a sample buffer invalidated its data.
- [var kCMSampleBufferError_RequiredParameterMissing: OSStatus](kcmsamplebuffererror_requiredparametermissing.md)
  An error code that indicates a required parameter’s value is invalid.
- [var kCMSampleBufferError_SampleIndexOutOfRange: OSStatus](kcmsamplebuffererror_sampleindexoutofrange.md)
  An error code that indicates the sample index is outside the range of samples that the buffer contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebuffererror_invalidmediaformat)*