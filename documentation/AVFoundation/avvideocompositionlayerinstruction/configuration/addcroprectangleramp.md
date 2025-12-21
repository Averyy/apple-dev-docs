# addCropRectangleRamp(_:)

**Framework**: AVFoundation  
**Kind**: method

Sets a crop rectangle ramp to apply during the specified time range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func addCropRectangleRamp(_ ramp: AVVideoCompositionLayerInstruction.CropRectangleRamp)
```

## See Also

- [func setCropRectangle(CGRect, at: CMTime)](avvideocompositionlayerinstruction/configuration/setcroprectangle(_:at:).md)
  Sets the crop rectangle value at a time within the time range of the instruction.
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/configuration/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addcroprectangleramp(_:))*