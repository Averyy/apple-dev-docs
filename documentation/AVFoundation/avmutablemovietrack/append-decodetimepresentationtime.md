# append(_:decodeTime:presentationTime:)

**Framework**: AVFoundation  
**Kind**: method

Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func append(_ sampleBuffer: CMSampleBuffer, decodeTime outDecodeTime: UnsafeMutablePointer<CMTime>?, presentationTime outPresentationTime: UnsafeMutablePointer<CMTime>?) throws
```

#### Discussion

If the sample buffer carries sample data, the sample data is written to the container specified by the track property [`mediaDataStorage`](avmutablemovietrack/mediadatastorage.md) if non-nil, or by the movie property [`defaultMediaDataStorage`](avmutablemovie/defaultmediadatastorage.md) if non-nil, and sample references are appended to the track’s media. If both media data storage properties are `nil`, the method will fail and return `NO`.

If the sample buffer carries sample references only, sample data will not be written and sample references to the samples in their original container are appended to the track’s media as necessary.

> **Note**:  In a track’s media, the first sample’s decode timestamp must be zero. For an audio track, each sample buffer’s duration is used as the sample decode duration. For other track types, the difference between a sample’s decode timestamp and the following sample’s decode timestamp is used as the first sample’s decode duration, so as to preserve the relative timing.

To make the new samples appear in the track’s timeline, invoke [`insertMediaTimeRange(_:into:)`](avmutablemovietrack/insertmediatimerange(_:into:).md). Retrieve the [`mediaPresentationTimeRange`](avmovietrack/mediapresentationtimerange.md) property before and after appending a sequence of samples, using [`CMTimeRangeGetEnd(_:)`](https://developer.apple.com/documentation/CoreMedia/CMTimeRangeGetEnd(_:)) on each to calculate the media time range for [`insertMediaTimeRange(_:into:)`](avmutablemovietrack/insertmediatimerange(_:into:).md).

It’s safe for multiple threads to call this method on different tracks at the same time.

## Parameters

- `sampleBuffer`: The sample buffer to be appended.
- `outDecodeTime`: A pointer to a   structure to receive the decode time in the media of the first sample appended from the sample buffer. Pass   if the information is not needed.
- `outPresentationTime`: A pointer to a   structure to receive the presentation time in the media of the first sample appended from the sample buffer. Pass   if the information is not needed.

## See Also

- [func insertMediaTimeRange(CMTimeRange, into: CMTimeRange) -> Bool](avmutablemovietrack/insertmediatimerange(_:into:).md)
  Inserts a reference to a media time range into a track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/append(_:decodetime:presentationtime:))*