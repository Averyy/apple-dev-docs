# insertMediaTimeRange(_:into:)

**Framework**: AVFoundation  
**Kind**: method

Inserts a reference to a media time range into a track.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func insertMediaTimeRange(_ mediaTimeRange: CMTimeRange, into trackTimeRange: CMTimeRange) -> Bool
```

#### Return Value

A Boolean value that indicates whether the insertion was successful.

#### Discussion

Use this method after appending samples or sample references to a track’s media. To specify that the media time range be played at its natural rate, pass `mediaTimeRange.duration == trackTimeRange.duration`; otherwise, the ratio between these is used to determine the playback rate. Pass [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) for `trackTimeRange.start` to indicate that the segment should be appended to the end of the track.

## Parameters

- `mediaTimeRange`: The presentation time range of the media to be inserted.
- `trackTimeRange`: The time range of the track into which the media is to be inserted.

## See Also

- [func append(CMSampleBuffer, decodeTime: UnsafeMutablePointer<CMTime>?, presentationTime: UnsafeMutablePointer<CMTime>?) throws](avmutablemovietrack/append(_:decodetime:presentationtime:).md)
  Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/insertmediatimerange(_:into:))*