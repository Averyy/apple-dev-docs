# AVVideoCompositionLayerInstruction.Configuration

**Framework**: AVFoundation  
**Kind**: struct

Configurable properties for initializing a new AVVideoCompositionLayerInstruction instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(assetTrack: AVAssetTrack)](avvideocompositionlayerinstruction/configuration/init(assettrack:).md)
  Creates a new video composition layer instruction for the given track.
- [init(trackID: CMPersistentTrackID)](avvideocompositionlayerinstruction/configuration/init(trackid:).md)
  Creates a new video composition layer instruction for the given track ID.
### Configuring the crop rectangle
- [func setCropRectangle(CGRect, at: CMTime)](avvideocompositionlayerinstruction/configuration/setcroprectangle(_:at:).md)
  Sets the crop rectangle value at a time within the time range of the instruction.
- [func addCropRectangleRamp(AVVideoCompositionLayerInstruction.CropRectangleRamp)](avvideocompositionlayerinstruction/configuration/addcroprectangleramp(_:).md)
  Sets a crop rectangle ramp to apply during the specified time range.
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/configuration/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.
### Configuring the opacity
- [func setOpacity(Float, at: CMTime)](avvideocompositionlayerinstruction/configuration/setopacity(_:at:).md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func addOpacityRamp(AVVideoCompositionLayerInstruction.OpacityRamp)](avvideocompositionlayerinstruction/configuration/addopacityramp(_:).md)
  Sets an opacity ramp to apply during a specified time range.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](avvideocompositionlayerinstruction/configuration/opacityramp(at:).md)
  Obtains the opacity ramp that includes a specified time.
### Configuring the transform
- [func setTransform(CGAffineTransform, at: CMTime)](avvideocompositionlayerinstruction/configuration/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.
- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](avvideocompositionlayerinstruction/configuration/addtransformramp(_:).md)
  Sets a transform ramp to apply during a given time range.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/configuration/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.
### Inspecting the configuration
- [var trackID: CMPersistentTrackID](avvideocompositionlayerinstruction/configuration/trackid.md)
  The track identifier of the source track to which the compositor will apply the instruction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(configuration: AVVideoCompositionLayerInstruction.Configuration)](avvideocompositionlayerinstruction/init(configuration:).md)
  Initialize an AVVideoCompositionLayerInstruction with a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration)*