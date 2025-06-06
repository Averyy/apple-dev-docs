# setOutputPresentationTimeStamp(_:)

**Framework**: Core Media  
**Kind**: method

Sets an output presentation timestamp to use in place of a calculated value.

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
func setOutputPresentationTimeStamp(_ pts: CMTime) throws
```

#### Discussion

This value is the time at which the system should present the decoded, trimmed, stretched and possibly reversed samples. By default, retrieving the value of the `outputPresentationTimeStamp` property calculates the time dynamically. You can use this method to set a specific value for `outputPresentationTimeStamp`.

For general forward playback in a scaled edit, calculate the timestamp as follows:

`((PresentationTimeStamp + TrimDurationAtStart - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime`

For general reversed playback, calculate the timestamp as shown below:

`((PresentationTimeStamp + Duration - TrimDurationAtEnd - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime`

## Parameters

- `pts`: The output presentation timestamp.

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
- [func sampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/sampletiminginfos.md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func sampleTimingInfo(at: CMItemIndex) throws -> CMSampleTimingInfo](cmsamplebuffer/sampletiminginfo(at:).md)
  Returns sample timing information for a sample at the specified index.
- [func outputSampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/outputsampletiminginfos.md)
  Retrieves an array of output sample timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/setoutputpresentationtimestamp(_:))*