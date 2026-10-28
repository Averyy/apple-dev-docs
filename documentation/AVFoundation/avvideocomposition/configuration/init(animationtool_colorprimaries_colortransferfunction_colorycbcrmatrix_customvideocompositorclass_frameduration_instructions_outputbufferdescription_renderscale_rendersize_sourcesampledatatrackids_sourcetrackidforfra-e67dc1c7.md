# init(animationTool:colorPrimaries:colorTransferFunction:colorYCbCrMatrix:customVideoCompositorClass:frameDuration:instructions:outputBufferDescription:renderScale:renderSize:sourceSampleDataTrackIDs:sourceTrackIDForFrameTiming:spatialVideoConfigurations:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

**Availability**:
- tvOS 26.0+

## Declaration

```swift
init(animationTool: AVVideoCompositionCoreAnimationTool? = nil, colorPrimaries: String? = nil, colorTransferFunction: String? = nil, colorYCbCrMatrix: String? = nil, customVideoCompositorClass: (any AVVideoCompositing.Type)? = nil, frameDuration: CMTime = CMTime.zero, instructions: [any AVVideoCompositionInstructionProtocol] = [any AVVideoCompositionInstructionProtocol](), outputBufferDescription: [[CMTag]]? = nil, renderScale: Float = 1.0, renderSize: CGSize = .zero, sourceSampleDataTrackIDs: [CMPersistentTrackID] = [CMPersistentTrackID](), sourceTrackIDForFrameTiming: Int32 = CMPersistentTrackID.zero, spatialVideoConfigurations: [AVSpatialVideoConfiguration] = [])
```

## See Also

### Creating a configuration
- [init(for: AVAsset, prototypeInstruction: AVVideoCompositionInstruction?) async throws](./init%28for,prototypeinstruction%29.md)
  Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](./init%28animationtool_colorprimaries_colortransferfunction_colorycbcrmatrix_customvideocompositorclass_frameduration_instructions_outputbufferdescription_perframehdrdisplaymetadatapolicy_renderscale_rendersize_sourcesampl-d13e75cb.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/init%28animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:renderscale:rendersize:sourcesampledatatrackids:sourcetrackidforframetiming:spatialvideoc-j1vm)*