# sourceFrame(byTrackID:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a source pixel buffer for the track that contains the specified identifier.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.9+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use sourceReadOnlyPixelBuffer(byTrackID:) instead

## Declaration

```swift
func sourceFrame(byTrackID trackID: CMPersistentTrackID) -> CVPixelBuffer?
```

```objc
- (CVPixelBufferRef) sourceFrameByTrackID:(CMPersistentTrackID) trackID;
```

#### Return Value

A pixel buffer, or `nil` if not found.

## Parameters

- `trackID`: The identifier of the track that contains the source frame.

## See Also

### Accessing source data
- [func attach(AVSpatialVideoConfiguration, to: inout CVMutablePixelBuffer) throws](./attach%28_,to%29.md)
  Associates the pixel buffer with the specified spatial configuration.
- [func sourceReadOnlyPixelBuffer(byTrackID: CMPersistentTrackID) -> CVReadOnlyPixelBuffer?](./sourcereadonlypixelbuffer%28bytrackid%29.md)
  Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [func sourceReadySampleBuffer(byTrackID: CMPersistentTrackID) -> CMReadySampleBuffer<CMSampleBuffer.DynamicContent>?](./sourcereadysamplebuffer%28bytrackid%29.md)
  Returns the source CMReadySampleBuffer for the given track ID.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](./sourcesamplebuffer%28bytrackid%29.md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](./sourcesampledatatrackids-3yiab.md)
  The identifiers of tracks that contain source sample data.
- [func sourceTaggedDynamicBuffers(byTrackID: CMPersistentTrackID) -> [CMTaggedDynamicBuffer]?](./sourcetaggeddynamicbuffers%28bytrackid%29.md)
  Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](./sourcetimedmetadata%28bytrackid%29.md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](./sourcetrackids.md)
  The identifiers of tracks that contain source video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest/sourceframe(bytrackid:))*