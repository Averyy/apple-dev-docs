# MTL4FXSpatialScaler

**Framework**: MetalFX  
**Kind**: protocol

An upscaling effect that generates a higher resolution texture in a render pass by spatially analyzing an input texture.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol MTL4FXSpatialScaler : MTLFXSpatialScalerBase
```

#### Overview

You create instances of this class by calling [`newSpatialScaler(with:compiler:)`](mtlfxspatialscalerdescriptor/newspatialscaler(with:compiler:).md).

When using instances of objects conforming to this protocol, you configure the different properties it inherits from protocol [`MTLFXSpatialScalerBase`](mtlfxspatialscalerbase.md) and then call [`encode(to:)`](mtl4fxspatialscaler/encode(to:).md) to encode its work into a Metal command buffer.

See [`MTLFXSpatialScalerBase`](mtlfxspatialscalerbase.md) for more details on configuring and using spatial scalers.

## Topics

### Instance Methods
- [func encode(to: any MTL4CommandBuffer)](mtl4fxspatialscaler/encode(to:).md)
  Encode this spatial scaler work into a command buffer.

## Relationships

### Inherits From
- [MTLFXSpatialScalerBase](mtlfxspatialscalerbase.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtl4fxspatialscaler)*