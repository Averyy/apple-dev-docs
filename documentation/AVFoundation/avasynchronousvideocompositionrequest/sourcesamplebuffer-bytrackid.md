# sourceSampleBuffer(byTrackID:)

**Framework**: AVFoundation  
**Kind**: method

Returns a source sample buffer for the track that contains the specified identifier.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func sourceSampleBuffer(byTrackID trackID: CMPersistentTrackID) -> CMSampleBuffer?
```

#### Return Value

A sample buffer, or `nil` if not found.

## Parameters

- `trackID`: The identifier of the track that contains the source sample data.

## See Also

- [var sourceTrackIDs: [NSNumber]](avasynchronousvideocompositionrequest/sourcetrackids.md)
  The identifiers of tracks that contain source video.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](avasynchronousvideocompositionrequest/sourcesampledatatrackids-3yiab.md)
  The identifiers of tracks that contain source sample data.
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](avasynchronousvideocompositionrequest/sourceframe(bytrackid:).md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid:).md)
  Returns a source timed metadata group for the track that contains the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcesamplebuffer(bytrackid:))*