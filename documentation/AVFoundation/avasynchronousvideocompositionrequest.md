# AVAsynchronousVideoCompositionRequest

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that contains information a video compositor needs to render an output pixel buffer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAsynchronousVideoCompositionRequest
```

```objc
@interface AVAsynchronousVideoCompositionRequest : NSObject
```

## Overview

The video compositor must adopt the [`AVVideoCompositing`](./avvideocompositing.md) protocol.

## Topics

### Inspecting the request
- [var compositionTime: CMTime](./avasynchronousvideocompositionrequest/compositiontime.md)
  A time for which to compose the frame.
- [var renderContext: AVVideoCompositionRenderContext](./avasynchronousvideocompositionrequest/rendercontext.md)
  The rendering context of the video composition.
- [var videoCompositionInstruction: any AVVideoCompositionInstructionProtocol](./avasynchronousvideocompositionrequest/videocompositioninstruction.md)
  A video composition instruction that indicates how to compose the frame.
### Accessing source data
- [func attach(AVSpatialVideoConfiguration, to: inout CVMutablePixelBuffer) throws](./avasynchronousvideocompositionrequest/attach%28_,to%29.md)
  Associates the pixel buffer with the specified spatial configuration.
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](./avasynchronousvideocompositionrequest/sourceframe%28bytrackid%29.md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceReadOnlyPixelBuffer(byTrackID: CMPersistentTrackID) -> CVReadOnlyPixelBuffer?](./avasynchronousvideocompositionrequest/sourcereadonlypixelbuffer%28bytrackid%29.md)
  Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [func sourceReadySampleBuffer(byTrackID: CMPersistentTrackID) -> CMReadySampleBuffer<CMSampleBuffer.DynamicContent>?](./avasynchronousvideocompositionrequest/sourcereadysamplebuffer%28bytrackid%29.md)
  Returns the source CMReadySampleBuffer for the given track ID.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](./avasynchronousvideocompositionrequest/sourcesamplebuffer%28bytrackid%29.md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](./avasynchronousvideocompositionrequest/sourcesampledatatrackids-3yiab.md)
  The identifiers of tracks that contain source sample data.
- [func sourceTaggedDynamicBuffers(byTrackID: CMPersistentTrackID) -> [CMTaggedDynamicBuffer]?](./avasynchronousvideocompositionrequest/sourcetaggeddynamicbuffers%28bytrackid%29.md)
  Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](./avasynchronousvideocompositionrequest/sourcetimedmetadata%28bytrackid%29.md)
  Returns a source timed metadata group for the track that contains the specified identifier.
- [var sourceTrackIDs: [NSNumber]](./avasynchronousvideocompositionrequest/sourcetrackids.md)
  The identifiers of tracks that contain source video.
- [- attachSpatialVideoConfiguration:toPixelBuffer:](./avasynchronousvideocompositionrequest/attachspatialvideoconfiguration_topixelbuffer_.md)
  Associates the pixel buffer with the specified spatial configuration.
- [sourceSampleDataTrackIDs](./avasynchronousvideocompositionrequest/sourcesampledatatrackids-9vxz5.md)
  The identifiers of tracks that contain source metadata.
- [- sourceTaggedBufferGroupByTrackID:](./avasynchronousvideocompositionrequest/sourcetaggedbuffergroupbytrackid_.md)
  Returns the source CMTaggedBufferGroupRef for the given track ID.
### Finishing the request
- [func finish(withComposedVideoFrame: CVPixelBuffer)](./avasynchronousvideocompositionrequest/finish%28withcomposedvideoframe%29.md)
  Finishes the request to compose the frame.
- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](./avasynchronousvideocompositionrequest/finish%28withcomposedpixelbuffer%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](./avasynchronousvideocompositionrequest/finish%28withcomposedtaggedbuffers%29.md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(with: any Error)](./avasynchronousvideocompositionrequest/finish%28with%29.md)
  Finishes the request with an error.
- [func finishCancelledRequest()](./avasynchronousvideocompositionrequest/finishcancelledrequest%28%29.md)
  Cancels the request to compose a video frame.
- [- finishWithComposedTaggedBufferGroup:](./avasynchronousvideocompositionrequest/finishwithcomposedtaggedbuffergroup_.md)
  The method that the custom compositor calls when composition succeeds.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Rendering the composition
- [func startRequest(AVAsynchronousVideoCompositionRequest)](./avvideocompositing/startrequest%28_%29.md)
  Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.
- [func cancelAllPendingVideoCompositionRequests()](./avvideocompositing/cancelallpendingvideocompositionrequests%28%29.md)
  Directs a custom video compositor object to cancel or finish all pending video composition requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest)*