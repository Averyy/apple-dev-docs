# sampleTimingInfo(at:)

**Framework**: Core Media  
**Kind**: method

Returns sample timing information for a sample at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func sampleTimingInfo(at sampleIndex: CMItemIndex) throws -> CMSampleTimingInfo
```

#### Return Value

A structure that contains the decode and presentation timestamps of a sample.

#### Discussion

The system throws a [`bufferHasNoSampleTimingInfo`](cmsamplebuffer/error/bufferhasnosampletiminginfo.md) error if the buffer doesn’t contain sample timing.

## Parameters

- `sampleIndex`: The index of the sample to query for sample timing. The system raises an error if the sample index is out of range.

## See Also

- [var duration: CMTime](cmsamplebuffer/duration.md)
  The total duration of a sample buffer.
- [var decodeTimeStamp: CMTime](cmsamplebuffer/decodetimestamp.md)
  The decode timestamp of the first sample in the buffer.
- [var presentationTimeStamp: CMTime](cmsamplebuffer/presentationtimestamp.md)
  The sample presentation timestamp that’s the earliest numerically in the sample buffer.
- [var outputDuration: CMTime](cmsamplebuffer/outputduration.md)
  The output duration of the sample buffer.
- [var outputDecodeTimeStamp: CMTime](cmsamplebuffer/outputdecodetimestamp.md)
  The output decode timestamp for a sample buffer.
- [var outputPresentationTimeStamp: CMTime](cmsamplebuffer/outputpresentationtimestamp.md)
  The output presentation timestamp of a sample buffer.
- [func setOutputPresentationTimeStamp(CMTime) throws](cmsamplebuffer/setoutputpresentationtimestamp(_:).md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func sampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/sampletiminginfos.md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func outputSampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/outputsampletiminginfos.md)
  Retrieves an array of output sample timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampletiminginfo(at:))*