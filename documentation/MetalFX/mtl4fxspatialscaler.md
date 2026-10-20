# MTL4FXSpatialScaler

**Framework**: MetalFX  
**Kind**: protocol  
**Role**: Protocol

An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+
- visionOS 26.0+

## Declaration

```swift
protocol MTL4FXSpatialScaler : MTLFXSpatialScalerBase
```

```objc
@protocol MTL4FXSpatialScaler <MTLFXSpatialScalerBase>
```

#### Overview

You create instances of this class by calling [`makeSpatialScaler(device:compiler:)`](./mtlfxspatialscalerdescriptor/makespatialscaler%28device,compiler%29.md).

When using instances of objects conforming to this protocol, you configure the different properties it inherits from protocol [`MTLFXSpatialScalerBase`](./mtlfxspatialscalerbase.md) and then call [`encode(commandBuffer:)`](./mtl4fxspatialscaler/encode%28commandbuffer%29.md) to encode its work into a Metal command buffer.

See [`MTLFXSpatialScalerBase`](./mtlfxspatialscalerbase.md) for more details on configuring and using spatial scalers.

## Topics

### Instance Methods
- [func encode(commandBuffer: any MTL4CommandBuffer)](./mtl4fxspatialscaler/encode%28commandbuffer%29.md)
  Encode this spatial scaler work into a command buffer.

## Relationships

### Inherits From
- [MTLFXSpatialScalerBase](./mtlfxspatialscalerbase.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtl4fxspatialscaler)*