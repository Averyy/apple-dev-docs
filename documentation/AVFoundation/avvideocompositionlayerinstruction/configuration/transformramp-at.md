# transformRamp(at:)

**Framework**: AVFoundation  
**Kind**: method

Obtains the transform ramp that includes a specified time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func transformRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?
```

## See Also

- [func setTransform(CGAffineTransform, at: CMTime)](avvideocompositionlayerinstruction/configuration/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.
- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](avvideocompositionlayerinstruction/configuration/addtransformramp(_:).md)
  Sets a transform ramp to apply during a given time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/transformramp(at:))*