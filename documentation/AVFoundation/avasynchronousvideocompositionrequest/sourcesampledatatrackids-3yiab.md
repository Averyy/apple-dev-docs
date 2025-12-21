# sourceSampleDataTrackIDs

**Framework**: AVFoundation  
**Kind**: property

The identifiers of tracks that contain source sample data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@nonobjc
var sourceSampleDataTrackIDs: [CMPersistentTrackID] { get }
```

#### Discussion

Sample data tracks have a media type of [`kCMMediaType_Metadata`](https://developer.apple.com/documentation/CoreMedia/kCMMediaType_Metadata).

## See Also

- [func attach(AVSpatialVideoConfiguration, to: inout CVMutablePixelBuffer) throws](avasynchronousvideocompositionrequest/attach(_:to:).md)
  Associates the pixel buffer with the specified spatial configuration.
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](avasynchronousvideocompositionrequest/sourceframe(bytrackid:).md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceReadOnlyPixelBuffer(byTrackID: CMPersistentTrackID) -> CVReadOnlyPixelBuffer?](avasynchronousvideocompositionrequest/sourcereadonlypixelbuffer(bytrackid:).md)
  Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [func sourceReadySampleBuffer(byTrackID: CMPersistentTrackID) -> CMReadySampleBuffer<CMSampleBuffer.DynamicContent>?](avasynchronousvideocompositionrequest/sourcereadysamplebuffer(bytrackid:).md)
  Returns the source CMReadySampleBuffer for the given track ID.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](avasynchronousvideocompositionrequest/sourcesamplebuffer(bytrackid:).md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [func sourceTaggedDynamicBuffers(byTrackID: CMPersistentTrackID) -> [CMTaggedDynamicBuffer]?](avasynchronousvideocompositionrequest/sourcetaggeddynamicbuffers(bytrackid:).md)
  Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid:).md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](avasynchronousvideocompositionrequest/sourcetrackids.md)
  The identifiers of tracks that contain source video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcesampledatatrackids-3yiab)*