# outputSampleTimingInfos()

**Framework**: Core Media  
**Kind**: method

Retrieves an array of output sample timing information structures that represents each sample in a sample buffer.

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
func outputSampleTimingInfos() throws -> [CMSampleTimingInfo]
```

#### Return Value

An array of structures that contain the output sample timing information.

#### Discussion

If the result contains a single element, it applies to all samples in the buffer.

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
- [func sampleTimingInfo(at: CMItemIndex) throws -> CMSampleTimingInfo](cmsamplebuffer/sampletiminginfo(at:).md)
  Returns sample timing information for a sample at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/outputsampletiminginfos())*