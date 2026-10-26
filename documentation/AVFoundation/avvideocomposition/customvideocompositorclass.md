# customVideoCompositorClass

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A custom compositor class to use.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var customVideoCompositorClass: (any AVVideoCompositing.Type)? { get }
```

```objc
@property (nonatomic, readonly, nullable) Class<AVVideoCompositing> * customVideoCompositorClass;
```

#### Discussion

The default is `nil`, which indicates to use the internal video compositor. The `customVideoCompositorClass` must implement the [`AVVideoCompositing`](../avvideocompositing.md) protocol.

## See Also

### Inspecting the video composition
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/customvideocompositorclass)*