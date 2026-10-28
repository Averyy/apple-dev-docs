# MEVideoDecoder

**Framework**: MediaExtension  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the requirements for a video decoder.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol MEVideoDecoder : NSObjectProtocol
```

```objc
@protocol MEVideoDecoder <NSObject>
```

## Overview

This protocol provides an interface for [Video Toolbox](../VideoToolbox/VideoToolbox.md) to create and interact with MediaExtension video decoders. `MEVideoDecoder` objects are always instantiated by Video Toolbox.

> **Note**:  Developers who wish to build MediaExtension video decoders using this API need to include a [Video decoder entitlement](./video-decoder-entitlement.md), provisioning profile, and specialized dictionary in their Info.plist file when building their extensions.
>
> For more information, see [Entitlements](../BundleResources/entitlements.md), [Create a development provisioning profile](https://developer.apple.com/help/account/manage-provisioning-profiles/create-a-development-provisioning-profile), and [Video decoder property list dictionary](./video-decoder-property-list-dictionary.md)

Once a user installs and runs the host app, embedded video decoder extensions become available to any app on the user’s system that opts in to using them by calling [`VTRegisterProfessionalVideoWorkflowVideoDecoders()`](../VideoToolbox/vtregisterprofessionalvideoworkflowvideodecoders%28%29.md).

> ❗ **Important**:  `MEVideoDecoder` objects run in a sandboxed process without access to the filesystem, network, and other kernel resources.

The following sections explain the video decoder life cycle and performing decoding operations.

### Creating a video decoder

The first time Video Toolbox opens a decoder in a process, it creates an instance of the [`MEVideoDecoderExtension`](./mevideodecoderextension.md) factory object. It then calls its [`makeVideoDecoder(codecType:videoFormatDescription:videoDecoderSpecifications:pixelBufferManager:)`](./mevideodecoderextension/makevideodecoder%28codectype,videoformatdescription,videodecoderspecifications,pixelbuffermanager%29.md) method for each decoder instance it needs. A decoder can evaluate the [`CMVideoCodecType`](../CoreMedia/cmvideocodectype.md) and [`CMVideoFormatDescription`](../CoreMedia/cmvideoformatdescription.md) that the system provides and confirm whether it can decode the specified format. If the decoder can’t decode the format, the factory routine needs to return the error [`MEError.Code.unsupportedFeature`](./meerror-swift.struct/code/unsupportedfeature.md). This sequence of events happens within [`VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)`](../VideoToolbox/vtdecompressionsessioncreate%28allocator,formatdescription,decoderspecification,imagebufferattributes,outputcallback,decompressionsessionout%29.md).

### Configuring a pixel buffer

Once instantiated, a decoder can call back to the provided [`MEVideoDecoderPixelBufferManager`](./mevideodecoderpixelbuffermanager.md) object to notify Video Toolbox of its output [CVPixelBuffer](../CoreVideo/cvpixelbuffer-q2e.md) requirements. It can make these calls multiple times if output requirements change in response to properties receiving new values or due to observed bitstream characteristics.

### Querying and setting properties

Properties can receive queries or new values on the decoder at any time, before, during or after frame decode, unless otherwise noted. These calls generally correspond to [`VTSessionSetProperty(_:key:value:)`](../VideoToolbox/vtsessionsetproperty%28_,key,value%29.md) and [`VTSessionCopyProperty(_:key:allocator:valueOut:)`](../VideoToolbox/vtsessioncopyproperty%28_,key,allocator,valueout%29.md) calls on the [`VTDecompressionSession`](../VideoToolbox/vtdecompressionsession.md) which opened the decoder. There may be cases where Video Toolbox directly sets or queries properties as well.

### Decoding frames

The framework serializes calls to [`decodeFrame(from:options:completionHandler:)`](./mevideodecoder/decodeframe%28from,options,completionhandler%29.md) and doesn’t send a new frame to the decoder until the last [`decodeFrame(from:options:completionHandler:)`](./mevideodecoder/decodeframe%28from,options,completionhandler%29.md) returns, unless decoding happens asynchronously. These calls correspond to [`VTDecompressionSessionDecodeFrame(_:sampleBuffer:flags:infoFlagsOut:outputHandler:)`](../VideoToolbox/vtdecompressionsessiondecodeframe%28_,samplebuffer,flags,infoflagsout,outputhandler%29.md) calls on the owning `VTDecompressionSession`.

Video decoders need to write their output frames into [CVPixelBuffer](../CoreVideo/cvpixelbuffer-q2e.md) objects allocated by the [`MEVideoDecoderPixelBufferManager`](./mevideodecoderpixelbuffermanager.md) object’s [`makePixelBuffer()`](./mevideodecoderpixelbuffermanager/makepixelbuffer%28%29.md) method. Obtaining pixel buffers from any other source may degrade performance or result in other issues.

If the decoder’s internal decoding queue is full and it can’t decode more frames, its [`isReadyForMoreMediaData`](./mevideodecoder/isreadyformoremediadata.md) property value returns [`false`](../Swift/false.md). It returns [`true`](../Swift/true.md) once the decoder can start accepting new frames again. This generally occurs after an earlier asynchronous frame completes.

### Handling format description changes

If a change occurs in the format description on incoming [`CMSampleBuffer`](../CoreMedia/cmsamplebuffer.md) objects, [Video Toolbox](../VideoToolbox/VideoToolbox.md) calls [`canAccept(_:)`](./mevideodecoder/canaccept%28_%29.md) to confirm whether the decoder can transition to the new format description. If that method response is [`false`](../Swift/false.md), the system usually closes the decoder and creates a new instance for the changed format description. A call to [`VTDecompressionSessionCanAcceptFormatDescription(_:formatDescription:)`](../VideoToolbox/vtdecompressionsessioncanacceptformatdescription%28_,formatdescription%29.md) can trigger a call of [`canAccept(_:)`](./mevideodecoder/canaccept%28_%29.md), or Video Toolbox calls this method if it sees a format description change on incoming `CMSampleBufferRef` objects.

## Topics

### Inspecting a video decoder
- [var contentHasInterframeDependencies: Bool](./mevideodecoder/contenthasinterframedependencies.md)
  A Boolean that specifies whether the content has interframe dependencies, if the decoder knows.
- [var recommendedThreadCount: Int](./mevideodecoder/recommendedthreadcount.md)
  The recommended number of threads for the decoder to use.
- [var actualThreadCount: Int](./mevideodecoder/actualthreadcount.md)
  The actual number of threads the decoder uses.
- [var supportedPixelFormatsOrderedByQuality: [NSNumber]](./mevideodecoder/supportedpixelformatsorderedbyquality.md)
  Provides hints about quality tradeoffs between pixel formats.
- [var reducedResolution: CGSize](./mevideodecoder/reducedresolution.md)
  A request to decode at a lower resolution than full-size.
- [var pixelFormatsWithReducedResolutionDecodeSupport: [NSNumber]](./mevideodecoder/pixelformatswithreducedresolutiondecodesupport.md)
  Provides a list of output pixel formats where the decoder supports reduced resolution decoding.
- [var producesRAWOutput: Bool](./mevideodecoder/producesrawoutput.md)
  Indicates whether the decoder produces RAW output which requires the use of a RAW processor.
- [var isReadyForMoreMediaData: Bool](./mevideodecoder/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the decoder to accept more sample buffers.
### Decoding frames
- [func canAccept(CMFormatDescription) -> Bool](./mevideodecoder/canaccept%28_%29.md)
  Asks the extension whether the decoder can decode frames with the format description that you specify.
- [func decodeFrame(from: CMSampleBuffer, options: MEDecodeFrameOptions, completionHandler: (CVImageBuffer?, MEDecodeFrameStatus, (any Error)?) -> Void)](./mevideodecoder/decodeframe%28from,options,completionhandler%29.md)
  Requests the extension to decode a video frame.
- [struct MEDecodeFrameStatus](./medecodeframestatus.md)
  A type that represents a non-error status related to a frame decode operation.
### Extension requirements
- [Video decoder property list dictionary](./video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](./video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.
### Notifications
- [MEVideoDecoderReadyForMoreMediaDataDidChangeNotification](./mevideodecoderreadyformoremediadatadidchangenotification.md)
  A notification that indicates a change to the decoder’s readiness to process additional media data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Video decoders
- [Supporting custom media formats and decoders](./supporting-custom-media-formats-and-decoders.md)
  Extend the media formats the system can open by providing a format reader and a video decoder.
- [protocol MEVideoDecoderExtension](./mevideodecoderextension.md)
  A protocol that defines a factory to create new video decoders for a codec type that the extension implements.
- [class MEDecodeFrameOptions](./medecodeframeoptions.md)
  An object that guides the video decoder operation on a per-frame basis.
- [class MEVideoDecoderPixelBufferManager](./mevideodecoderpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [Video decoder property list dictionary](./video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](./video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoder)*