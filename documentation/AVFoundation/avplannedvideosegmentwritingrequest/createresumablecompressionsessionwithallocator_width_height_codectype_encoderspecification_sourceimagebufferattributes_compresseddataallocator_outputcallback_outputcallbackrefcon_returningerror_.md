# createResumableCompressionSessionWithAllocator:width:height:codecType:encoderSpecification:sourceImageBufferAttributes:compressedDataAllocator:outputCallback:outputCallbackRefCon:returningError:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Helper function to create a VTCompressionSession that restores the video encoder state persisted at the end of the previous segment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
- (VTCompressionSessionRef) createResumableCompressionSessionWithAllocator:(CFAllocatorRef) allocator width:(int32_t) width height:(int32_t) height codecType:(CMVideoCodecType) codecType encoderSpecification:(NSDictionary *) encoderSpecification sourceImageBufferAttributes:(NSDictionary *) sourceImageBufferAttributes compressedDataAllocator:(CFAllocatorRef) compressedDataAllocator outputCallback:(VTCompressionOutputCallback) outputCallback outputCallbackRefCon:(void *) outputCallbackRefCon returningError:(NSError **) errorOut;
```

## Discussion

Clients using VTCompressionSession directly to produce encoded video samples for writing the segment must use this method to create the session. The client should perform additional configurations on the returned compression session, but must apply the same configurations for each segment of the track.

Client cannot call this method more than once on a writing request object. For the same segment writing request, this method and the resumableAssetWriterInputWithMediaType:outputSettings:sourceFormatHint:returningError: method are mutually exclusive. The client can call either one of the two, but not both. This method fails (returns nil) with error if the parameters differ from the previous segment.

The client should release the session after use. The writing request retains the compression session but does not mutate the session after this method is returned.

## Parameters

- `allocator`: An allocator for the session. Pass NULL to use the default allocator.
- `width`: The pixel width of video frames.
- `height`: The pixel height of video frames.
- `codecType`: The codec type.
- `encoderSpecification`: A dictionary describing the characteristics of a video encoder to use. Pass NULL to let the system choose an encoder. If the client provides a specification, it should omit the following keys: kVTCompressionPropertyKey_SourceFrameCount, kVTCompressionPropertyKey_MoreFramesBeforeStart, and kVTCompressionPropertyKey_MoreFramesAfterEnd, since such keys will be overwritten by the underlying implementation.
- `sourceImageBufferAttributes`: Required attributes for source pixel buffers, used when creating a pixel buffer pool for source frames. If you don’t want the system to create one for you, pass NULL. Using pixel buffers not allocated by the system increases the chance that you’ll have to copy image data.
- `compressedDataAllocator`: An allocator for the compressed data. Pass NULL to use the default allocator. In macOS 10.12 and later, using a compressedDataAllocator may trigger an extra buffer copy.
- `outputCallback`: The callback to invoke with compressed frames. The system may call this function asynchronously, on a different thread from the one that calls VTCompressionSessionEncodeFrame. Pass NULL only if you’ll be calling VTCompressionSessionEncodeFrameWithOutputHandler for encoding frames.
- `outputCallbackRefCon`: Client-defined reference value for the output callback.
- `errorOut`: A pointer where a NSError object may be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest/createresumablecompressionsessionwithallocator:width:height:codectype:encoderspecification:sourceimagebufferattributes:compresseddataallocator:outputcallback:outputcallbackrefcon:returningerror:)*