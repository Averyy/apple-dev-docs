# sourceTaggedBufferGroupByTrackID:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the source CMTaggedBufferGroupRef for the given track ID.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (CMTaggedBufferGroupRef) sourceTaggedBufferGroupByTrackID:(CMPersistentTrackID) trackID;
```

#### Discussion

Returns nil if the video track does not contain tagged buffers. Returns nil if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.

## Parameters

- `trackID`: The track ID for the requested source tagged buffer group.

## See Also

### Accessing source data
- [- attachSpatialVideoConfiguration:toPixelBuffer:](./attachspatialvideoconfiguration_topixelbuffer_.md)
  Associates the pixel buffer with the specified spatial configuration.
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](./sourceframe%28bytrackid%29.md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](./sourcesamplebuffer%28bytrackid%29.md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [sourceSampleDataTrackIDs](./sourcesampledatatrackids-9vxz5.md)
  The identifiers of tracks that contain source metadata.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](./sourcetimedmetadata%28bytrackid%29.md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](./sourcetrackids.md)
  The identifiers of tracks that contain source video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcetaggedbuffergroupbytrackid:)*