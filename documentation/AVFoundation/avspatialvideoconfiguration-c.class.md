# AVSpatialVideoConfiguration

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An AVSpatialVideoConfiguration specifies spatial video properties.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface AVSpatialVideoConfiguration : NSObject
```

## Topics

### Creating a configuration
- [- init](./avspatialvideoconfiguration-c.class/init.md)
- [- initWithFormatDescription:](./avspatialvideoconfiguration-c.class/initwithformatdescription_.md)
  Initializes an AVSpatialVideoConfiguration with a format description.
### Modifying the configuration
- [cameraCalibrationDataLensCollection](./avspatialvideoconfiguration-c.class/cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [cameraSystemBaseline](./avspatialvideoconfiguration-c.class/camerasystembaseline.md)
  Specifies the distance between centers of the lenses of the camera system that created the video.
- [disparityAdjustment](./avspatialvideoconfiguration-c.class/disparityadjustment.md)
  Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [horizontalFieldOfView](./avspatialvideoconfiguration-c.class/horizontalfieldofview.md)
  Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Inspecting the video composition
- [var renderSize: CGSize](./avvideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./avvideocomposition/renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](./avvideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./avvideocomposition/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [var colorPrimaries: String?](./avvideocomposition/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](./avvideocomposition/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](./avvideocomposition/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](./avvideocomposition/customvideocompositorclass.md)
  A custom compositor class to use.
- [outputBufferDescription](./avvideocomposition/outputbufferdescription-3wsar.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.
- [spatialVideoConfigurations](./avvideocomposition/spatialvideoconfigurations-2ipps.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-c.class)*