# addTransformRamp(_:)

**Framework**: AVFoundation  
**Kind**: method

Sets a transform ramp to apply during a given time range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func addTransformRamp(_ ramp: AVVideoCompositionLayerInstruction.TransformRamp)
```

## See Also

- [func setTransform(CGAffineTransform, at: CMTime)](avvideocompositionlayerinstruction/configuration/settransform(_:at:).md)
  Sets the transform value at a time within the time range of the instruction.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/configuration/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addtransformramp(_:))*