# AVSpatialVideoConfiguration

**Framework**: AVFoundation  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AVSpatialVideoConfiguration
```

## Topics

### Creating a configuration
- [init()](avspatialvideoconfiguration-swift.struct/init.md)
  Initializes an AVSpatialVideoConfiguration instance with all the properties set to nil.
- [init(formatDescription: CMFormatDescription)](avspatialvideoconfiguration-swift.struct/init(formatdescription:).md)
  Initializes an AVSpatialVideoConfiguration with a format description.
- [static var nonSpatial: AVSpatialVideoConfiguration](avspatialvideoconfiguration-swift.struct/nonspatial.md)
  A non-spatial video configuration.
### Modifying the configuration
- [var cameraCalibrationDataLensCollection: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection?](avspatialvideoconfiguration-swift.struct/cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [var cameraSystemBaseline: UInt32?](avspatialvideoconfiguration-swift.struct/camerasystembaseline.md)
  Specifies the distance between centers of the lenses of the camera system that created the video.
- [var disparityAdjustment: Int32?](avspatialvideoconfiguration-swift.struct/disparityadjustment.md)
  Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [var horizontalFieldOfView: UInt32?](avspatialvideoconfiguration-swift.struct/horizontalfieldofview.md)
  Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var spatialVideoConfigurations: [AVSpatialVideoConfiguration]](avvideocomposition/spatialvideoconfigurations-80iab.md)
  Indicates the spatial configurations that are available to associate with the output of the video composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct)*