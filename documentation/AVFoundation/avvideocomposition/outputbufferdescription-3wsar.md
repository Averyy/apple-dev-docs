# outputBufferDescription

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSArray * outputBufferDescription;
```

#### Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) and ProjectionKind must be specified. The behavior is undefined if the output tagged buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. An exception will be thrown if the objects in the array are not of type CMTagCollectionRef. Note that tagged buffers are only supported for custom compositors.

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
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](./customvideocompositorclass.md)
  A custom compositor class to use.
- [spatialVideoConfigurations](./spatialvideoconfigurations-2ipps.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.
- [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-c.class.md)
  An AVSpatialVideoConfiguration specifies spatial video properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/outputbufferdescription-3wsar)*