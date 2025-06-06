# presentationTimeStamp

**Framework**: Core Media  
**Kind**: property

The sample presentation timestamp that’s the earliest numerically in the sample buffer.

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
var presentationTimeStamp: CMTime { get }
```

#### Discussion

For in-presentation-order samples, the value represents the presentation timestamp of the first sample. For out-of-presentation-order samples, it represents the presentation timestamp of the sample the system presents first, which isn’t necessarily the first sample in the buffer.

This value is [`invalid`](cmtime/invalid.md) if there’s an error.

## See Also

- [var duration: CMTime](cmsamplebuffer/duration.md)
  The total duration of a sample buffer.
- [var decodeTimeStamp: CMTime](cmsamplebuffer/decodetimestamp.md)
  The decode timestamp of the first sample in the buffer.
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
- [func outputSampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/outputsampletiminginfos.md)
  Retrieves an array of output sample timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/presentationtimestamp)*