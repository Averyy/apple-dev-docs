# setTransform(_:at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the transform value at a time within the time range of the instruction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func setTransform(_ transform: CGAffineTransform, at time: CMTime)
```

## See Also

### Configuring the transform
- [func addTransformRamp(AVVideoCompositionLayerInstruction.TransformRamp)](./addtransformramp%28_%29.md)
  Sets a transform ramp to apply during a given time range.
- [func transformRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.TransformRamp?](./transformramp%28at%29.md)
  Obtains the transform ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/settransform(_:at:))*