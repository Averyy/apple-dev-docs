# AVAsynchronousVideoCompositionRequest

**Framework**: AVFoundation  
**Kind**: class

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

#### Overview

The video compositor must adopt the [`AVVideoCompositing`](avvideocompositing.md) protocol.

## Topics

### Inspecting the Request
- [var compositionTime: CMTime](avasynchronousvideocompositionrequest/compositiontime.md)
  A time for which to compose the frame.
- [var renderContext: AVVideoCompositionRenderContext](avasynchronousvideocompositionrequest/rendercontext.md)
  The rendering context of the video composition.
- [var videoCompositionInstruction: any AVVideoCompositionInstructionProtocol](avasynchronousvideocompositionrequest/videocompositioninstruction.md)
  A video composition instruction that indicates how to compose the frame.
### Accessing Source Data
- [var sourceTrackIDs: [NSNumber]](avasynchronousvideocompositionrequest/sourcetrackids.md)
  The identifiers of tracks that contain source video.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](avasynchronousvideocompositionrequest/sourcesampledatatrackids-3yiab.md)
  The identifiers of tracks that contain source sample data.
- [func sourceFrame(byTrackID: CMPersistentTrackID) -> CVPixelBuffer?](avasynchronousvideocompositionrequest/sourceframe(bytrackid:).md)
  Returns a source pixel buffer for the track that contains the specified identifier.
- [func sourceSampleBuffer(byTrackID: CMPersistentTrackID) -> CMSampleBuffer?](avasynchronousvideocompositionrequest/sourcesamplebuffer(bytrackid:).md)
  Returns a source sample buffer for the track that contains the specified identifier.
- [func sourceTimedMetadata(byTrackID: CMPersistentTrackID) -> AVTimedMetadataGroup?](avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid:).md)
  Returns a source timed metadata group for the track that contains the specified identifier.
### Finishing the Request
- [func finish(withComposedVideoFrame: CVPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedvideoframe:).md)
  Finishes the request to compose the frame.
- [func finish(with: any Error)](avasynchronousvideocompositionrequest/finish(with:).md)
  Finishes the request with an error.
- [func finishCancelledRequest()](avasynchronousvideocompositionrequest/finishcancelledrequest.md)
  Cancels the request to compose a video frame.
### Instance Methods
- [func finish(withComposedPixelBuffer: CVReadOnlyPixelBuffer)](avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer:).md)
  The method that the custom compositor calls when composition succeeds.
- [func finish(withComposedTaggedBuffers: [CMTaggedDynamicBuffer])](avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers:).md)
  The method that the custom compositor calls when composition succeeds.  - Parameter taggedBuffers: The tagged buffers containing the composed tagged buffers. The tagged buffers must be compatible with the outputBufferDescription specified in the video composition. The outputBufferDescription must not be nil when calling this function.
- [func finish(withTaggedBuffers: [CMTaggedBuffer])](avasynchronousvideocompositionrequest/finish(withtaggedbuffers:).md)
  The method that the custom compositor calls when composition succeeds.
- [func sourceReadOnlyPixelBuffer(byTrackID: CMPersistentTrackID) -> CVReadOnlyPixelBuffer?](avasynchronousvideocompositionrequest/sourcereadonlypixelbuffer(bytrackid:).md)
  Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [func sourceReadySampleBuffer(byTrackID: CMPersistentTrackID) -> CMReadySampleBuffer<CMSampleBuffer.DynamicContent>?](avasynchronousvideocompositionrequest/sourcereadysamplebuffer(bytrackid:).md)
  Returns the source CMReadySampleBuffer for the given track ID.
- [func sourceTaggedBuffers(byTrackID: CMPersistentTrackID) -> [CMTaggedBuffer]?](avasynchronousvideocompositionrequest/sourcetaggedbuffers(bytrackid:).md)
  Returns the source tagged buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [func sourceTaggedDynamicBuffers(byTrackID: CMPersistentTrackID) -> [CMTaggedDynamicBuffer]?](avasynchronousvideocompositionrequest/sourcetaggeddynamicbuffers(bytrackid:).md)
  Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func startRequest(AVAsynchronousVideoCompositionRequest)](avvideocompositing/startrequest(_:).md)
  Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.
- [func cancelAllPendingVideoCompositionRequests()](avvideocompositing/cancelallpendingvideocompositionrequests.md)
  Directs a custom video compositor object to cancel or finish all pending video composition requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest)*