# AVVideoCompositionLayerInstruction.Configuration

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Configurable properties for initializing a new AVVideoCompositionLayerInstruction instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(assetTrack: AVAssetTrack)](./configuration/init%28assettrack%29.md)
  Creates a new video composition layer instruction for the given track.
- [init(trackID: CMPersistentTrackID)](./configuration/init%28trackid%29.md)
  Creates a new video composition layer instruction for the given track ID.
### Configuring the crop rectangle
- [func setCropRectangle(CGRect, at: CMTime)](./configuration/setcroprectangle%28_,at%29.md)
  Sets the crop rectangle value at a time within the time range of the instruction.
- [func addCropRectangleRamp(AVVideoCompositionLayerInstruction.CropRectangleRamp)](./configuration/addcroprectangleramp%28_%29.md)
  Sets a crop rectangle ramp to apply during the specified time range.
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](./configuration/croprectangleramp%28at%29.md)
  Obtains the crop rectangle ramp that includes the specified time.
### Configuring the opacity
- [func setOpacity(Float, at: CMTime)](./configuration/setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func addOpacityRamp(AVVideoCompositionLayerInstruction.OpacityRamp)](./configuration/addopacityramp%28_%29.md)
  Sets an opacity ramp to apply during a specified time range.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](./configuration/opacityramp%28at%29.md)
  Obtains the opacity ramp that includes a specified time.
### Configuring the transform
- [func setTransform(CGAffineTransform, at: CMTime)](./configuration/settransform%28_,at%29.md)
  Sets the transform value at a time within the time range of the instruction.
- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](./configuration/addtransformramp%28_%29.md)
  Sets a transform ramp to apply during a given time range.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](./configuration/transformramp%28at%29.md)
  Obtains the transform ramp that includes a specified time.
### Inspecting the configuration
- [var trackID: CMPersistentTrackID](./configuration/trackid.md)
  The track identifier of the source track to which the compositor will apply the instruction.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a layer instruction
- [convenience init(configuration: AVVideoCompositionLayerInstruction.Configuration)](./init%28configuration%29.md)
  Initialize an AVVideoCompositionLayerInstruction with a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration)*