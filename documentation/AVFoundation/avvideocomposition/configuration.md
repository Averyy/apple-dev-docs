# AVVideoComposition.Configuration

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Configurable properties for initializing a new AVVideoComposition instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(for: AVAsset, prototypeInstruction: AVVideoCompositionInstruction?) async throws](./configuration/init%28for,prototypeinstruction%29.md)
  Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](./configuration/init%28animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_perframehdrdisplaymetadatapolicy_renderscale_rendersize_sourcesampl-d13e75cb.md)
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](./configuration/init%28animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_renderscale_rendersize_sourcesampledatatrackids_sourcetrackidforfra-e67dc1c7.md)
### Inspecting the configuration
- [var renderSize: CGSize](./configuration/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./configuration/renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](./configuration/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./configuration/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [var colorPrimaries: String?](./configuration/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](./configuration/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](./configuration/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](./configuration/customvideocompositorclass.md)
  A custom compositor class to use.
- [var outputBufferDescription: [[CMTag]]?](./configuration/outputbufferdescription.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [var instructions: [any AVVideoCompositionInstructionProtocol]](./configuration/instructions.md)
  The video composition instructions.
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](./configuration/spatialvideoconfigurations.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](./configuration/perframehdrdisplaymetadatapolicy.md)
  The policy for display of HDR display metadata on the rendered frame.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](./configuration/sourcesampledatatrackids.md)
  The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [var sourceTrackIDForFrameTiming: CMPersistentTrackID](./configuration/sourcetrackidforframetiming.md)
  An identifier of the source track from which the video composition derives frame timing.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a video composition
- [convenience init(configuration: AVVideoComposition.Configuration)](./init%28configuration%29.md)
  Initialize an AVVideoComposition with a configuration.
- [convenience init(applyingFiltersTo: AVAsset, applier: (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws](./init%28applyingfiltersto,applier%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./videocomposition%28with,applyingcifilterswithhandler,completionhandler%29.md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [struct AVCIImageFilteringParameters](../avciimagefilteringparameters.md)
- [struct AVCIImageFilteringResult](../avciimagefilteringresult.md)
  An output video frame processed with Core Image filtering.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](./videocomposition%28withpropertiesof,completionhandler%29.md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](./init%28propertiesof%29.md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](./init%28asset,applyingcifilterswithhandler%29.md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration)*