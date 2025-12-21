# init(for:prototypeInstruction:)

**Framework**: AVFoundation  
**Kind**: init

Initializes a video composition configuration with the specified asset properties and optional prototype video composition instruction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) init(for asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction? = nil) async throws
```

## Parameters

- `asset`: Asset to use with the video composition
- `prototypeInstruction`: A video composition instruction to use as a prototype.

## See Also

- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](avvideocomposition/configuration/init(animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:perframehdrdisplaymetadatapolicy:renderscale:rendersize:sourcesampledatatrackids:sourcetr-2lwnx.md)
- [init(animationTool: AVVideoCompositionCoreAnimationTool?, colorPrimaries: String?, colorTransferFunction: String?, colorYCbCrMatrix: String?, customVideoCompositorClass: (any AVVideoCompositing.Type)?, frameDuration: CMTime, instructions: [any AVVideoCompositionInstructionProtocol], outputBufferDescription: [[CMTag]]?, renderScale: Float, renderSize: CGSize, sourceSampleDataTrackIDs: [CMPersistentTrackID], sourceTrackIDForFrameTiming: Int32, spatialVideoConfigurations: [AVSpatialVideoConfiguration])](avvideocomposition/configuration/init(animationtool:colorprimaries:colortransferfunction:colorycbcrmatrix:customvideocompositorclass:frameduration:instructions:outputbufferdescription:renderscale:rendersize:sourcesampledatatrackids:sourcetrackidforframetiming:spatialvideoc-j1vm.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/init(for:prototypeinstruction:))*