# AVVideoComposition.Configuration

**Framework**: AVFoundation  
**Kind**: struct

Configurable properties for initializing a new AVVideoComposition instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(for: AVAsset, prototypeInstruction: AVVideoCompositionInstruction?) async throws](avvideocomposition/configuration/init(for:prototypeinstruction:).md)
  Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](avvideocomposition/configuration/init(animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:perframehdrdisplaymetadatapolicy:renderscale:rendersize:sourcesampledatatrackids:sourcetr-2lwnx.md)
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](avvideocomposition/configuration/init(animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:renderscale:rendersize:sourcesampledatatrackids:sourcetrackidforframetiming:spatialvideoc-j1vm.md)
### Inspecting the configuration
- [var renderSize: CGSize](avvideocomposition/configuration/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](avvideocomposition/configuration/renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](avvideocomposition/configuration/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](avvideocomposition/configuration/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [var colorPrimaries: String?](avvideocomposition/configuration/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](avvideocomposition/configuration/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](avvideocomposition/configuration/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](avvideocomposition/configuration/customvideocompositorclass.md)
  A custom compositor class to use.
- [var outputBufferDescription: [[CMTag]]?](avvideocomposition/configuration/outputbufferdescription.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [var instructions: [any AVVideoCompositionInstructionProtocol]](avvideocomposition/configuration/instructions.md)
  The video composition instructions.
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](avvideocomposition/configuration/spatialvideoconfigurations.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](avvideocomposition/configuration/perframehdrdisplaymetadatapolicy.md)
  The policy for display of HDR display metadata on the rendered frame.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](avvideocomposition/configuration/sourcesampledatatrackids.md)
  The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [var sourceTrackIDForFrameTiming: CMPersistentTrackID](avvideocomposition/configuration/sourcetrackidforframetiming.md)
  An identifier of the source track from which the video composition derives frame timing.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(configuration: AVVideoComposition.Configuration)](avvideocomposition/init(configuration:).md)
  Initialize an AVVideoComposition with a configuration.
- [convenience init(applyingFiltersTo: AVAsset, applier: (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws](avvideocomposition/init(applyingfiltersto:applier:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [class func videoComposition(with: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:).md)
  Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [class AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md)
  An object that supports using Core Image filters to process an individual video frame in a video composition.
- [struct AVCIImageFilteringParameters](avciimagefilteringparameters.md)
- [struct AVCIImageFilteringResult](avciimagefilteringresult.md)
  An output video frame processed with Core Image filtering.
- [class func videoComposition(withPropertiesOf: AVAsset, completionHandler: (AVVideoComposition?, (any Error)?) -> Void)](avvideocomposition/videocomposition(withpropertiesof:completionhandler:).md)
  Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [init(propertiesOf: AVAsset)](avvideocomposition/init(propertiesof:).md)
  Creates a video composition object configured to present the video tracks of the specified asset.
- [init(asset: AVAsset, applyingCIFiltersWithHandler: (AVAsynchronousCIImageFilteringRequest) -> Void)](avvideocomposition/init(asset:applyingcifilterswithhandler:).md)
  Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration)*