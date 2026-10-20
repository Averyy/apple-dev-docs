# opacityRamp(at:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Obtains the opacity ramp that includes a specified time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func opacityRamp(at time: CMTime) -> AVVideoCompositionLayerInstruction.OpacityRamp?
```

## See Also

### Configuring the opacity
- [func setOpacity(Float, at: CMTime)](./setopacity%28_,at%29.md)
  Sets the opacity value at a specific time within the time range of the instruction.
- [func addOpacityRamp(AVVideoCompositionLayerInstruction.OpacityRamp)](./addopacityramp%28_%29.md)
  Sets an opacity ramp to apply during a specified time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionlayerinstruction/configuration/opacityramp(at:))*