# MEVideoDecoder

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines the requirements for a video decoder.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol MEVideoDecoder : NSObjectProtocol
```

#### Overview

This protocol provides an interface for [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) to create and interact with MediaExtension video decoders. `MEVideoDecoder` objects are always instantiated by Video Toolbox.

> **Note**:  Developers who wish to build MediaExtension video decoders using this API need to include a [`Video decoder entitlement`](video-decoder-entitlement.md), provisioning profile, and specialized dictionary in their Info.plist file when building their extensions. For more information, see [`Entitlements`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements), [`Create a development provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-provisioning-profiles/create-a-development-provisioning-profile), and [`Video decoder property list dictionary`](video-decoder-property-list-dictionary.md)

Once a user installs and runs the host app, embedded video decoder extensions become available to any app on the user’s system that opts in to using them by calling [`VTRegisterProfessionalVideoWorkflowVideoDecoders()`](https://developer.apple.com/documentation/VideoToolbox/VTRegisterProfessionalVideoWorkflowVideoDecoders()).

> ❗ **Important**:  `MEVideoDecoder` objects run in a sandboxed process without access to the filesystem, network, and other kernel resources.

The following sections explain the video decoder life cycle and performing decoding operations.

##### Creating a Video Decoder

The first time Video Toolbox opens a decoder in a process, it creates an instance of the [`MEVideoDecoderExtension`](mevideodecoderextension.md) factory object. It then calls its [`makeVideoDecoder(codecType:videoFormatDescription:videoDecoderSpecifications:pixelBufferManager:)`](mevideodecoderextension/makevideodecoder(codectype:videoformatdescription:videodecoderspecifications:pixelbuffermanager:).md) method for each decoder instance it needs. A decoder can evaluate the [`CMVideoCodecType`](https://developer.apple.com/documentation/CoreMedia/CMVideoCodecType) and [`CMVideoFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMVideoFormatDescription) that the system provides and confirm whether it can decode the specified format. If the decoder can’t decode the format, the factory routine needs to return the error [`MEError.Code.unsupportedFeature`](meerror-swift.struct/code/unsupportedfeature.md). This sequence of events happens within [`VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)).

##### Configuring a Pixel Buffer

Once instantiated, a decoder can call back to the provided [`MEVideoDecoderPixelBufferManager`](mevideodecoderpixelbuffermanager.md) object to notify Video Toolbox of its output [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) requirements. It can make these calls multiple times if output requirements change in response to properties receiving new values or due to observed bitstream characteristics.

##### Querying and Setting Properties

Properties can receive queries or new values on the decoder at any time, before, during or after frame decode, unless otherwise noted. These calls generally correspond to [`VTSessionSetProperty(_:key:value:)`](https://developer.apple.com/documentation/VideoToolbox/VTSessionSetProperty(_:key:value:)) and [`VTSessionCopyProperty(_:key:allocator:valueOut:)`](https://developer.apple.com/documentation/VideoToolbox/VTSessionCopyProperty(_:key:allocator:valueOut:)) calls on the [`VTDecompressionSession`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSession) which opened the decoder. There may be cases where Video Toolbox directly sets or queries properties as well.

##### Decoding Frames

The framework serializes calls to [`decodeFrame(from:options:completionHandler:)`](mevideodecoder/decodeframe(from:options:completionhandler:).md) and doesn’t send a new frame to the decoder until the last [`decodeFrame(from:options:completionHandler:)`](mevideodecoder/decodeframe(from:options:completionhandler:).md) returns, unless decoding happens asynchronously. These calls correspond to [`VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:infoFlagsOut:outputHandler:)`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:infoFlagsOut:outputHandler:)) calls on the owning `VTDecompressionSession`.

Video decoders need to write their output frames into [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) objects allocated by the [`MEVideoDecoderPixelBufferManager`](mevideodecoderpixelbuffermanager.md) object’s [`makePixelBuffer()`](mevideodecoderpixelbuffermanager/makepixelbuffer().md) method. Obtaining pixel buffers from any other source may degrade performance or result in other issues.

If the decoder’s internal decoding queue is full and it can’t decode more frames, its [`isReadyForMoreMediaData`](mevideodecoder/isreadyformoremediadata.md) property value returns [`false`](https://developer.apple.com/documentation/Swift/false). It returns [`true`](https://developer.apple.com/documentation/Swift/true) once the decoder can start accepting new frames again. This generally occurs after an earlier asynchronous frame completes.

##### Handling Format Description Changes

If a change occurs in the format description on incoming [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) objects, [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) calls [`canAccept(_:)`](mevideodecoder/canaccept(_:).md) to confirm whether the decoder can transition to the new format description. If that method response is [`false`](https://developer.apple.com/documentation/Swift/false), the system usually closes the decoder and creates a new instance for the changed format description. A call to [`VTDecompressionSessionCanAcceptFormatDescription(_:formatDescription:)`](https://developer.apple.com/documentation/VideoToolbox/VTDecompressionSessionCanAcceptFormatDescription(_:formatDescription:)) can trigger a call of [`canAccept(_:)`](mevideodecoder/canaccept(_:).md), or Video Toolbox calls this method if it sees a format description change on incoming `CMSampleBufferRef` objects.

## Topics

### Inspecting a video decoder
- [var contentHasInterframeDependencies: Bool](mevideodecoder/contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var recommendedThreadCount: Int](mevideodecoder/recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](mevideodecoder/actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](mevideodecoder/supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var reducedResolution: CGSize](mevideodecoder/reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](mevideodecoder/pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](mevideodecoder/producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](mevideodecoder/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.
### Decoding frames
- [func canAccept(CMFormatDescription) -> Bool](mevideodecoder/canaccept(_:).md)
  Asks the extension whether the decoder can decode frames with the format description that you specify.
- [func decodeFrame(from: CMSampleBuffer, options: MEDecodeFrameOptions, completionHandler: (CVImageBuffer?, MEDecodeFrameStatus, (any Error)?) -> Void)](mevideodecoder/decodeframe(from:options:completionhandler:).md)
  Requests the extension to decode a video frame.
- [struct MEDecodeFrameStatus](medecodeframestatus.md)
  A type that represents a non-error status related to a frame decode operation.
### Extension requirements
- [Video decoder property list dictionary](video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MEVideoDecoderExtension](mevideodecoderextension.md)
  A protocol that defines a factory to create new video decoders for a codec type that the extension implements.
- [class MEDecodeFrameOptions](medecodeframeoptions.md)
  An object that guides the video decoder operation on a per-frame basis.
- [class MEVideoDecoderPixelBufferManager](mevideodecoderpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [Video decoder property list dictionary](video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder)*