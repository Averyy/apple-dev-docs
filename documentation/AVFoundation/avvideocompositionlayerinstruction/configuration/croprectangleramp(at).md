# cropRectangleRamp(at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Obtains the crop rectangle ramp that includes the specified time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func cropRectangleRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?
```

## See Also

### Configuring the crop rectangle
- [func setCropRectangle(CGRect, at: CMTime)](./setcroprectangle%28_,at%29.md)
  Sets the crop rectangle value at a time within the time range of the instruction.
- [func addCropRectangleRamp(AVVideoCompositionLayerInstruction.CropRectangleRamp)](./addcroprectangleramp%28_%29.md)
  Sets a crop rectangle ramp to apply during the specified time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/croprectangleramp(at:))*