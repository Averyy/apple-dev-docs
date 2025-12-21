# setCropRectangle(_:at:)

**Framework**: AVFoundation  
**Kind**: method

Sets the crop rectangle value at a time within the time range of the instruction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func setCropRectangle(_ rect: CGRect, at time: CMTime)
```

## See Also

- [func addCropRectangleRamp(AVVideoCompositionLayerInstruction.CropRectangleRamp)](avvideocompositionlayerinstruction/configuration/addcroprectangleramp(_:).md)
  Sets a crop rectangle ramp to apply during the specified time range.
- [func cropRectangleRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.CropRectangleRamp?](avvideocompositionlayerinstruction/configuration/croprectangleramp(at:).md)
  Obtains the crop rectangle ramp that includes the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/setcroprectangle(_:at:))*