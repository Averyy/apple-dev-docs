# AVVideoCompositionLayerInstruction.Configuration

**Framework**: AVFoundation  
**Kind**: struct

Configurable properties for initializing a new AVVideoCompositionLayerInstruction instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(assetTrack: AVAssetTrack)](avvideocompositionlayerinstruction/configuration/init(assettrack:).md)
  Creates a new video composition layer instruction for the given track.
- [init(trackID: CMPersistentTrackID)](avvideocompositionlayerinstruction/configuration/init(trackid:).md)
  Creates a new video composition layer instruction for the given track ID.
### Instance Properties
- [var trackID: CMPersistentTrackID](avvideocompositionlayerinstruction/configuration/trackid.md)
  The track identifier of the source track to which the compositor will apply the instruction.
### Instance Methods
- [func addCropRectangleRamp(AVVideoCompositionLayerInstruction.CropRectangleRamp)](avvideocompositionlayerinstruction/configuration/addcroprectangleramp(_:).md)
  Sets a crop rectangle ramp to apply during the specified time range.
- [func addOpacityRamp(AVVideoCompositionLayerInstruction.OpacityRamp)](avvideocompositionlayerinstruction/configuration/addopacityramp(_:).md)
  Sets an opacity ramp to apply during a specified time range.
- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](avvideocompositionlayerinstruction/configuration/addtransformramp(_:).md)
  Sets a transform ramp to apply during a given time range.
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/configuration/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](avvideocompositionlayerinstruction/configuration/opacityramp(at:).md)
  Obtains the opacity ramp that includes a specified time.
- [func setCropRectangle(CGRect, at: CMTime)](avvideocompositionlayerinstruction/configuration/setcroprectangle(_:at:).md)
  Sets the crop rectangle value at a time within the time range of the instruction.
- [func setOpacity(Float, at: CMTime)](avvideocompositionlayerinstruction/configuration/setopacity(_:at:).md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func setTransform(CGAffineTransform, at: CMTime)](avvideocompositionlayerinstruction/configuration/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/configuration/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration)*