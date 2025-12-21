# outputBufferDescription

**Framework**: AVFoundation  
**Kind**: property

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var outputBufferDescription: [[CMTag]]? { get }
```

#### Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) and ProjectionKind must be specified. The behavior is undefined if the output buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. Note that tagged buffers are only supported for custom compositors.

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
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](avvideocomposition/spatialvideoconfigurations-80iab.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [struct AVSpatialVideoConfiguration](avspatialvideoconfiguration-swift.struct.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/outputbufferdescription-3ayt8)*