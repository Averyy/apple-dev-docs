# sourceSampleDataTrackIDs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifiers of tracks that contain source metadata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * sourceSampleDataTrackIDs;
```

## Discussion

The track identifiers are of type [`kCMMediaType_Metadata`](../../CoreMedia/kcmmediatype_metadata.md).

## See Also

### Accessing source data
- [- attachSpatialVideoConfiguration:toPixelBuffer:](./attachspatialvideoconfiguration_topixelbuffer_.md)
  Associates the pixel buffer with the specified spatial configuration.
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](./sourceframe%28bytrackid%29.md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](./sourcesamplebuffer%28bytrackid%29.md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [- sourceTaggedBufferGroupByTrackID:](./sourcetaggedbuffergroupbytrackid_.md)
  Returns the source CMTaggedBufferGroupRef for the given track ID.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](./sourcetimedmetadata%28bytrackid%29.md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](./sourcetrackids.md)
  The identifiers of tracks that contain source video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourcesampledatatrackids-9vxz5)*