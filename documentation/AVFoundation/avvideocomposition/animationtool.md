# animationTool

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A video composition tool to use with Core Animation in offline rendering.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var animationTool: AVVideoCompositionCoreAnimationTool? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) AVVideoCompositionCoreAnimationTool * animationTool;
```

#### Discussion

This attribute may be `nil`. Set an animation tool if you’re using the composition in conjunction with [`AVAssetExportSession`](../avassetexportsession.md) for offline rendering, rather than with [`AVPlayer`](../avplayer.md).

## See Also

### Inspecting the video composition
- [var renderSize: CGSize](./rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](./frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var colorPrimaries: String?](./colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](./colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](./colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](./customvideocompositorclass.md)
  A custom compositor class to use.
- [var outputBufferDescription: [[CMTag]]?](./outputbufferdescription-3ayt8.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of an array of CMTag objects that describes the output buffers.
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](./spatialvideoconfigurations-80iab.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [struct AVSpatialVideoConfiguration](../avspatialvideoconfiguration-swift.struct.md)
- [outputBufferDescription](./outputbufferdescription-3wsar.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.
- [spatialVideoConfigurations](./spatialvideoconfigurations-2ipps.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-c.class.md)
  An AVSpatialVideoConfiguration specifies spatial video properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/animationtool)*