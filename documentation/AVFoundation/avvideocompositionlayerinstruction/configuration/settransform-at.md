# setTransform(_:at:)

**Framework**: AVFoundation  
**Kind**: method

Sets the transform value at a time within the time range of the instruction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func setTransform(_ transform: CGAffineTransform, at time: CMTime)
```

## See Also

- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](avvideocompositionlayerinstruction/configuration/addtransformramp(_:).md)
  Sets a transform ramp to apply during a given time range.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](avvideocompositionlayerinstruction/configuration/transformramp(at:).md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/settransform(_:at:))*