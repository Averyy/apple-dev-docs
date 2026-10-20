# transformRamp(at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Obtains the transform ramp that includes a specified time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func transformRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?
```

## See Also

### Configuring the transform
- [func setTransform(CGAffineTransform, at: CMTime)](./settransform%28_,at%29.md)
  Sets the transform value at a time within the time range of the instruction.
- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](./addtransformramp%28_%29.md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/transformramp(at:))*