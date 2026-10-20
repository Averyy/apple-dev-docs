# MTLFXTemporalDenoisedScaler

**Framework**: MetalFX  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
protocol MTLFXTemporalDenoisedScaler : MTLFXTemporalDenoisedScalerBase
```

```objc
@protocol MTLFXTemporalDenoisedScaler <MTLFXTemporalDenoisedScalerBase>
```

## Topics

### Instance Methods
- [func encode(commandBuffer: any MTLCommandBuffer)](./mtlfxtemporaldenoisedscaler/encode%28commandbuffer%29.md)
  Encode this scaler denoiser’s work into a command buffer.

## Relationships

### Inherits From
- [MTLFXFrameInterpolatableScaler](./mtlfxframeinterpolatablescaler.md)
- [MTLFXTemporalDenoisedScalerBase](./mtlfxtemporaldenoisedscalerbase.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscaler)*