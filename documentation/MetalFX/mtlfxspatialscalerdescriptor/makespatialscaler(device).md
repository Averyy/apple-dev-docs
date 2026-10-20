# makeSpatialScaler(device:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Instance Method

Creates a spatial scaler instance from this descriptor’s current property values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+
- visionOS 1.0+

## Declaration

```swift
func makeSpatialScaler(device: any MTLDevice) -> (any MTLFXSpatialScaler)?
```

```objc
- (id<MTLFXSpatialScaler>) newSpatialScalerWithDevice:(id<MTLDevice>) device;
```

## Parameters

- `device`: An [`MTLDevice`](../../Metal/mtldevice.md) instance that represents the GPU that applies the spatial scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/makespatialscaler(device:))*