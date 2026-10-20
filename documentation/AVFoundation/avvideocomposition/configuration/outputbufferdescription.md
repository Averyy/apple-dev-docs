# outputBufferDescription

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var outputBufferDescription: [[CMTag]]? { get set }
```

#### Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) and ProjectionKind must be specified. The behavior is undefined if the output buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. Note that tagged buffers are only supported for custom compositors.

## See Also

### Inspecting the configuration
- [var renderSize: CGSize](./rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](./frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [var colorPrimaries: String?](./colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](./colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](./colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](./customvideocompositorclass.md)
  A custom compositor class to use.
- [var instructions: [any AVVideoCompositionInstructionProtocol]](./instructions.md)
  The video composition instructions.
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](./spatialvideoconfigurations.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [var perFrameHDRDisplayMetadataPolicy: AVVideoComposition.PerFrameHDRDisplayMetadataPolicy](./perframehdrdisplaymetadatapolicy.md)
  The policy for display of HDR display metadata on the rendered frame.
- [var sourceSampleDataTrackIDs: [CMPersistentTrackID]](./sourcesampledatatrackids.md)
  The identifiers of source sample data tracks in the composition that the object requires to compose frames.
- [var sourceTrackIDForFrameTiming: CMPersistentTrackID](./sourcetrackidforframetiming.md)
  An identifier of the source track from which the video composition derives frame timing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/configuration/outputbufferdescription)*