# init(for:prototypeInstruction:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated(nonsending)
init(for asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction? = nil) async throws
```

## Parameters

- `asset`: Asset to use with the video composition
- `prototypeInstruction`: A video composition instruction to use as a prototype.

## See Also

### Creating a configuration
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](./init%28animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_perframehdrdisplaymetadatapolicy_renderscale_rendersize_sourcesampl-d13e75cb.md)
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](./init%28animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_renderscale_rendersize_sourcesampledatatrackids_sourcetrackidforfra-e67dc1c7.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/init(for:prototypeinstruction:))*