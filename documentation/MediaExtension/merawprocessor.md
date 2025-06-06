# MERAWProcessor

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines the requirements for a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
protocol MERAWProcessor : NSObjectProtocol
```

#### Overview

This protocol provides an interface for [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) to create and interact with MediaExtension RAW processors. [`MERAWProcessor`](merawprocessor.md) objects are instantiated by Video Toolbox and are closely linked to a corresponding [`MEVideoDecoder`](mevideodecoder.md) object that produces RAW video output.

> **Note**:  Developers who wish to build MediaExtension RAW processors using this API need to include a [`RAW processor entitlement`](raw-processor-entitlement.md), provisioning profile, and specialized dictionary in their Info.plist file when building their extensions. For more information, see [`Entitlements`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements), [`Create a development provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-provisioning-profiles/create-a-development-provisioning-profile), and [`RAW processor property list dictionary`](raw-processor-property-list-dictionary.md).

 Developers who wish to build MediaExtension RAW processors using this API need to include a [`RAW processor entitlement`](raw-processor-entitlement.md), provisioning profile, and specialized dictionary in their Info.plist file when building their extensions.

For more information, see [`Entitlements`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/entitlements), [`Create a development provisioning profile`](https://developer.apple.comhttps://developer.apple.com/help/account/manage-provisioning-profiles/create-a-development-provisioning-profile), and [`RAW processor property list dictionary`](raw-processor-property-list-dictionary.md).

Once a user installs and runs the host app, embedded RAW processor extensions become available to any app on the user’s system that opts in to using them by calling [`VTRegisterProfessionalVideoWorkflowVideoDecoders()`](https://developer.apple.com/documentation/VideoToolbox/VTRegisterProfessionalVideoWorkflowVideoDecoders()).

> ❗ **Important**:  `MERAWProcessor` objects run in a sandboxed process without access to the filesystem, network, and other kernel resources.

 `MERAWProcessor` objects run in a sandboxed process without access to the filesystem, network, and other kernel resources.

MediaExtension RAW processor’s operation and life cycle closely tie to [`VTRAWProcessingSession`](https://developer.apple.com/documentation/VideoToolbox/VTRAWProcessingSession).

##### Creating a Raw Processor

An instance of the [`MERAWProcessorExtension`](merawprocessorextension.md) factory object is created the first time the given processor is opened by Video Toolbox in a process. The [`makeProcessor(formatDescription:pixelBufferManager:)`](merawprocessorextension/makeprocessor(formatdescription:pixelbuffermanager:).md) method on the [`MERAWProcessorExtension`](merawprocessorextension.md) object will be called once for each processor instance needed. The processor can evaluate the provided [`CMVideoFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMVideoFormatDescription) at this point and confirm whether it is able to process the specified format. If the processor cannot process the format, the factory routine should return [`MEError.Code.unsupportedFeature`](meerror-swift.struct/code/unsupportedfeature.md). This sequence of calls will happen inside of [`VTRAWProcessingSession`](https://developer.apple.com/documentation/VideoToolbox/VTRAWProcessingSession).

##### Configuring Pixel Buffer Requirements

At any point after instantiation, the processor can call back into the provided [`MERAWProcessorPixelBufferManager`](merawprocessorpixelbuffermanager.md) object to notify Video Toolbox of its output pixel buffer requirements. The processor extension may make multiple calls if output requirements change in response to properties being set or due to observed bitstream characteristics.

##### Processing Frames

Calls to [`processFrame(fromImageBuffer:completionHandler:)`](merawprocessor/processframe(fromimagebuffer:completionhandler:).md) are serialized. A new frame is not sent to the processor until the last [`processFrame(fromImageBuffer:completionHandler:)`](merawprocessor/processframe(fromimagebuffer:completionhandler:).md) has returned, but may be submitted before the [`processFrame(fromImageBuffer:completionHandler:)`](merawprocessor/processframe(fromimagebuffer:completionhandler:).md) completion handler is called if the processing is happening asynchronously. These calls correspond to [`VTRAWProcessingSessionProcessFrame`](https://developer.apple.com/documentation/VideoToolbox/VTRAWProcessingSessionProcessFrame) calls on the parent `VTRAWProcessingSession`.

RAW processors must write their output frames into `CVPixelBuffers` allocated through the [`makePixelBuffer()`](merawprocessorpixelbuffermanager/makepixelbuffer().md) interface. Returning [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) from any other source may result in degraded performance or other issues.

If the processor’s internal processing queue is full, and it cannot process more frames, it should return [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO) when the [`isReadyForMoreMediaData`](merawprocessor/isreadyformoremediadata.md) property is queried. This property should return [`YES`](https://developer.apple.com/documentation/ObjectiveC/YES) again when the processor is able to accept new frames – generally after an earlier asynchronous frame processing operation is completed.

## Topics

### Inspecting a RAW processor
- [var metalDeviceRegistryID: UInt64](merawprocessor/metaldeviceregistryid.md)
  Requests the processor use the provided Metal device for processing.
- [var outputColorAttachments: [String : Any]](merawprocessor/outputcolorattachments.md)
  Returns the color-related Core Video image buffer keys and values that become attachments to the output pixel buffers.
- [var processingParameters: [MERAWProcessingParameter]](merawprocessor/processingparameters.md)
  Provides a list of processing parameters that can be changed by the client of Video Toolbox session to influence processing behavior.
- [var isReadyForMoreMediaData: Bool](merawprocessor/isreadyformoremediadata.md)
  Indicates the readiness of the processor to accept more sample buffers.
### Processing RAW frame
- [func processFrame(fromImageBuffer: CVPixelBuffer, completionHandler: (CVPixelBuffer?, (any Error)?) -> Void)](merawprocessor/processframe(fromimagebuffer:completionhandler:).md)
  Requests the processor to process a video frame.
### Extension requirements
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MERAWProcessorExtension](merawprocessorextension.md)
  A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- [class MERAWProcessorPixelBufferManager](merawprocessorpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [class MERAWProcessingParameter](merawprocessingparameter.md)
  An object for the RAW processor to describe each processing parameter the processor exposes.
- [enum MERAWProcessorNotification](merawprocessornotification.md)
  Notifications that indicate a RAW processor state change.
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessor)*