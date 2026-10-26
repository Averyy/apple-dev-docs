# attachSpatialVideoConfiguration:toPixelBuffer:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Associates the pixel buffer with the specified spatial configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) attachSpatialVideoConfiguration:(AVSpatialVideoConfiguration *) spatialVideoConfiguration toPixelBuffer:(CVPixelBufferRef) pixelBuffer;
```

## Parameters

- `spatialVideoConfiguration`: The spatial configuration to associate with the pixel buffer.
- `pixelBuffer`: The pixel buffer to associate with the spatial configuration. NOTE: The spatial configuration must be one of the spatial configurations specified in the `AVVideoComposition/spatialConfigurations` property. An exception will be thrown otherwise. NOTE: All pixel buffers from the custom compositor must be associated with the same spatial configuration. An exception will be thrown otherwise. A spatial configuration with all nil values indicates the video is not spatial. A nil spatial configuration also indicates the video is not spatial. The value can be nil, which indicates the output will not be spatial, but a spatial configuration with all nil values must be in the `AVVideoComposition/spatialConfigurations` property or an exception will be thrown.

## See Also

### Accessing source data
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](./sourceframe%28bytrackid%29.md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](./sourcesamplebuffer%28bytrackid%29.md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [sourceSampleDataTrackIDs](./sourcesampledatatrackids-9vxz5.md)
  The identifiers of tracks that contain source metadata.
- [- sourceTaggedBufferGroupByTrackID:](./sourcetaggedbuffergroupbytrackid_.md)
  Returns the source CMTaggedBufferGroupRef for the given track ID.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](./sourcetimedmetadata%28bytrackid%29.md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](./sourcetrackids.md)
  The identifiers of tracks that contain source video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/attachspatialvideoconfiguration:topixelbuffer:)*