# sampleTimingInfoInvalid

**Framework**: Core Media  
**Kind**: property  
**Role**: Type Property

The sample buffer unexpectedly contains nonnumeric sample timing information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let sampleTimingInfoInvalid: NSError
```

## See Also

### Errors
- [static let allocationFailed: NSError](./allocationfailed.md)
  The system failed to allocate memory.
- [static let alreadyHasDataBuffer: NSError](./alreadyhasdatabuffer.md)
  You attempted to set data on a sample buffer that already contains media data.
- [static let arrayTooSmall: NSError](./arraytoosmall.md)
  The output array isn’t large enough to hold the requested array.
- [static let bufferHasNoSampleSizes: NSError](./bufferhasnosamplesizes.md)
  You requested sample sizes on a buffer that doesn’t provide that information.
- [static let bufferHasNoSampleTimingInfo: NSError](./bufferhasnosampletiminginfo.md)
  You requested sample timing on a buffer that doesn’t contain that information.
- [static let bufferNotReady: NSError](./buffernotready.md)
  The system can’t make the buffer’s data ready for use.
- [static let cannotSubdivide: NSError](./cannotsubdivide.md)
  A sample buffer doesn’t contain sample sizes.
- [static let dataCanceled: NSError](./datacanceled.md)
  A sample buffer canceled its data loading operation.
- [static let dataFailed: NSError](./datafailed.md)
  A sample buffer failed to load its data.
- [static let invalidEntryCount: NSError](./invalidentrycount.md)
  A timing or size value isn’t within the allowed range.
- [static let invalidMediaFormat: NSError](./invalidmediaformat.md)
  The format of the media doesn’t match the sample buffer’s format description.
- [static let invalidMediaTypeForOperation: NSError](./invalidmediatypeforoperation.md)
  The media type the format description defines isn’t value for the requested operation.
- [static let invalidSampleData: NSError](./invalidsampledata.md)
  The sample buffer contains bad data.
- [static let invalidated: NSError](./invalidated.md)
  A sample buffer invalidated its data.
- [static let requiredParameterMissing: NSError](./requiredparametermissing.md)
  You didn’t provide a valid value for a required parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/error/sampletiminginfoinvalid)*