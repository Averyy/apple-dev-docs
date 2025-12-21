# spatialVideoConfigurations

**Framework**: AVFoundation  
**Kind**: property

Indicates the spatial configurations that are available to associate with the output of the video composition.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var spatialVideoConfigurations: [AVSpatialVideoConfiguration] { get }
```

#### Discussion

A custom compositor can output spatial video by specifying one of these spatial configurations. A spatial configuration with all nil values indicates the video is not spatial. A nil spatial configuration also indicates the video is not spatial. The value can be nil, which indicates the output will not be spatial. NOTE: If this property is not empty, then the client must attach one of the spatial configurations in this array to all of the pixel buffers, otherwise an exception will be thrown.

## See Also

- [var renderSize: CGSize](avvideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](avvideocomposition/renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](avvideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](avvideocomposition/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [var colorPrimaries: String?](avvideocomposition/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](avvideocomposition/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](avvideocomposition/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](avvideocomposition/customvideocompositorclass.md)
  A custom compositor class to use.
- [var outputBufferDescription: [[CMTag]]?](avvideocomposition/outputbufferdescription-3ayt8.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [struct AVSpatialVideoConfiguration](avspatialvideoconfiguration-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/spatialvideoconfigurations-80iab)*