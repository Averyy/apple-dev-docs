# attach(_:to:)

**Framework**: AVFoundation  
**Kind**: method

Associates the pixel buffer with the specified spatial configuration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func attach(_ spatialVideoConfiguration: AVSpatialVideoConfiguration, to pixelBuffer: inout CVMutablePixelBuffer) throws
```

## Parameters

- `spatialVideoConfiguration`: The spatial configuration to associate with the pixel buffer.
- `pixelBuffer`: The pixel buffer to associate with the spatial configuration.   NOTE: The spatial configuration must be one of the spatial configurations specified in the AVVideoComposition’s spatialConfigurations property. An exception will be thrown otherwise.   NOTE: All pixel buffers from the custom compositor must be associated with the same spatial configuration. An exception will be thrown otherwise.   Specify a value of .nonSpatial for spatialVideoConfiguration to indicate the video is not spatial, but note that a .nonSpatial configuration must be in the   property or an exception will be thrown.

## See Also

- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](avasynchronousvideocompositionrequest/sourceframe(bytrackid:).md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceReadOnlyPixelBuffer(byTrackID: CMPersistentTrackID) -> CVReadOnlyPixelBuffer?](avasynchronousvideocompositionrequest/sourcereadonlypixelbuffer(bytrackid:).md)
  Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [func sourceReadySampleBuffer(byTrackID: CMPersistentTrackID) -> CMReadySampleBuffer<CMSampleBuffer.DynamicContent>?](avasynchronousvideocompositionrequest/sourcereadysamplebuffer(bytrackid:).md)
  Returns the source CMReadySampleBuffer for the given track ID.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](avasynchronousvideocompositionrequest/sourcesamplebuffer(bytrackid:).md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](avasynchronousvideocompositionrequest/sourcesampledatatrackids-3yiab.md)
  The identifiers of tracks that contain source sample data.
- [func sourceTaggedDynamicBuffers(byTrackID: CMPersistentTrackID) -> [CMTaggedDynamicBuffer]?](avasynchronousvideocompositionrequest/sourcetaggeddynamicbuffers(bytrackid:).md)
  Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid:).md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](avasynchronousvideocompositionrequest/sourcetrackids.md)
  The identifiers of tracks that contain source video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/attach(_:to:))*