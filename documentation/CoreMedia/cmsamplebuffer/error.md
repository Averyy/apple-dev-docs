# CMSampleBuffer.Error

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that defines errors that occur during framework operations.

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
struct Error
```

## Topics

### Errors
- [static let allocationFailed: NSError](./error/allocationfailed.md)
  The system failed to allocate memory.
- [static let alreadyHasDataBuffer: NSError](./error/alreadyhasdatabuffer.md)
  You attempted to set data on a sample buffer that already contains media data.
- [static let arrayTooSmall: NSError](./error/arraytoosmall.md)
  The output array isn’t large enough to hold the requested array.
- [static let bufferHasNoSampleSizes: NSError](./error/bufferhasnosamplesizes.md)
  You requested sample sizes on a buffer that doesn’t provide that information.
- [static let bufferHasNoSampleTimingInfo: NSError](./error/bufferhasnosampletiminginfo.md)
  You requested sample timing on a buffer that doesn’t contain that information.
- [static let bufferNotReady: NSError](./error/buffernotready.md)
  The system can’t make the buffer’s data ready for use.
- [static let cannotSubdivide: NSError](./error/cannotsubdivide.md)
  A sample buffer doesn’t contain sample sizes.
- [static let dataCanceled: NSError](./error/datacanceled.md)
  A sample buffer canceled its data loading operation.
- [static let dataFailed: NSError](./error/datafailed.md)
  A sample buffer failed to load its data.
- [static let invalidEntryCount: NSError](./error/invalidentrycount.md)
  A timing or size value isn’t within the allowed range.
- [static let invalidMediaFormat: NSError](./error/invalidmediaformat.md)
  The format of the media doesn’t match the sample buffer’s format description.
- [static let invalidMediaTypeForOperation: NSError](./error/invalidmediatypeforoperation.md)
  The media type the format description defines isn’t value for the requested operation.
- [static let invalidSampleData: NSError](./error/invalidsampledata.md)
  The sample buffer contains bad data.
- [static let invalidated: NSError](./error/invalidated.md)
  A sample buffer invalidated its data.
- [static let requiredParameterMissing: NSError](./error/requiredparametermissing.md)
  You didn’t provide a valid value for a required parameter.
- [static let sampleIndexOutOfRange: NSError](./error/sampleindexoutofrange.md)
  You specified a sample index that’s outside of the range of samples that the buffer contains.
- [static let sampleTimingInfoInvalid: NSError](./error/sampletiminginfoinvalid.md)
  The sample buffer unexpectedly contains nonnumeric sample timing information.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [CMSampleBuffer.Flags](./flags.md)
  Flags that customize the behavior of framework operations.
- [CMSampleBuffer.NotificationKey](./notificationkey.md)
  A key for sample buffer notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/error)*