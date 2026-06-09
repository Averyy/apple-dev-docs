# createResumableCompressionSession(width:height:codecType:encoderSpecification:sourceImageBufferAttributes:outputHandler:)

**Framework**: AVFoundation  
**Kind**: method

Helper function to create a VTCompressionSession that restores the video encoder state persisted at the end of the previous segment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func createResumableCompressionSession(width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: [String : any Sendable]? = nil, sourceImageBufferAttributes: [String : any Sendable]? = nil, outputHandler: @escaping @Sendable (OSStatus, VTEncodeInfoFlags, CMSampleBuffer?) -> Void) throws -> VTCompressionSession
```

#### Return Value

A configured VTCompressionSession ready for encoding this segment.

#### Discussion

Clients using VTCompressionSession directly to produce encoded video samples for writing the segment must use this method to create the session. The client should perform additional configurations on the returned compression session, but must apply the same configurations for each segment of the track.

Client cannot call this method more than once on a writing request object. For the same segment writing request, this method and the makeResumableWriterInput method are mutually exclusive. The client can call either one of the two, but not both. This method fails (returns nil) with error if the parameters differ from the previous segment.

The client should release the session after use. The writing request retains the compression session but does not mutate the session after this method is returned.

> **Note**: An error if the session cannot be created or if parameters differ from previous segment.

## Parameters

- `width`: The pixel width of video frames.
- `height`: The pixel height of video frames.
- `codecType`: The codec type.
- `encoderSpecification`: A dictionary describing the characteristics of a video encoder to use. Pass nil to let the system choose an encoder. If the client provides a specification, it should omit the following keys kVTCompressionPropertyKey_SourceFrameCount, kVTCompressionPropertyKey_MoreFramesBeforeStart, kVTCompressionPropertyKey_MoreFramesAfterEnd since such keys will be overwritten by the underlying implementation.
- `sourceImageBufferAttributes`: Required attributes for source pixel buffers, used when creating a pixel buffer pool for source frames. If you don’t want the system to create one for you, pass nil. Using pixel buffers not allocated by the system increases the chance that you’ll have to copy image data.
- `outputHandler`: The handler to invoke with compressed frames. The system may call this function asynchronously, on a different thread from the one that calls VTCompressionSessionEncodeFrame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplannedvideosegmentwritingrequest/createresumablecompressionsession(width:height:codectype:encoderspecification:sourceimagebufferattributes:outputhandler:))*