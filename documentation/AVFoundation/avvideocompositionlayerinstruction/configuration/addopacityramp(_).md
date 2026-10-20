# addOpacityRamp(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets an opacity ramp to apply during a specified time range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func addOpacityRamp(_ ramp: AVVideoCompositionLayerInstruction.OpacityRamp)
```

## See Also

### Configuring the opacity
- [func setOpacity(Float, at: CMTime)](./setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func opacityRamp(at: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?](./opacityramp%28at%29.md)
  Obtains the opacity ramp that includes a specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/addopacityramp(_:))*