# append(_:)

**Framework**: AVFoundation  
**Kind**: method

Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func append(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> (decodeTime: CMTime, presentationTime: CMTime)
```

#### Return Value

A tuple containing the decodeTime & presentationTime.

- decodeTime: CMTime structure to receive the decode time in the media of the first sample appended from the sample buffer.
- presentationTime: CMTime structure to receive the presentation time in the media of the first sample appended from the sample buffer. Pass NULL if you do not need this information.

#### Discussion

If the ready sample buffer carries sample data, the sample data is written to the container specified by the track property mediaDataStorage if non-nil, or else by the movie property defaultMediaDataStorage if non-nil, and sample references will be appended to the track’s media. If both media data storage properties are nil, the method will fail with an error.

If the sample buffer carries sample references only, sample data will not be written and sample references to the samples in their original container will be appended to the track’s media as necessary. Note regarding sample timing: in a track’s media, the first sample’s decode timestamp must always be zero. For an audio track, each sample buffer’s duration is used as the sample decode duration. For other track types, difference between a sample’s decode timestamp and the following sample’s decode timestamp is used as the first sample’s decode duration, so as to preserve the relative timing.

Note that this method does not modify the track’s sourceTimeMappings but only appends sample references and sample data to the track’s media. To make the new samples appear in the track’s timeline, invoke -insertMediaTimeRange:intoTimeRange:. You can retrieve the mediaPresentationTimeRange property before and after appending a sequence of samples, using CMTimeRangeGetEnd on each to calculate the media TimeRange for -insertMediaTimeRange:intoTimeRange:.

Note that this method expects

- the sample buffer’s media type must match with track’s media type
- the sample buffer must contain encoded video (should not contain image buffers)
- the sample buffer must contain encoded media data (should not contain caption groups)

It’s safe for multiple threads to call this method on different tracks at once.

> **Note**: This method throws AVErrorDiskFull if the device containing the track’s media data storage is full.

## Parameters

- `sampleBuffer`: The CMReadySampleBuffer to be appended; this may be obtained from an instance of AVAssetReader.

## See Also

- [func append(CMSampleBuffer, decodeTime: UnsafeMutablePointer<CMTime>?, presentationTime: UnsafeMutablePointer<CMTime>?) throws](avmutablemovietrack/append(_:decodetime:presentationtime:).md)
  Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.
- [func insertMediaTimeRange(CMTimeRange, into: CMTimeRange) -> Bool](avmutablemovietrack/insertmediatimerange(_:into:).md)
  Inserts a reference to a media time range into a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/append(_:))*