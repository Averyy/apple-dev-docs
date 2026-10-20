# makeTemporalScaler(device:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Instance Method

Creates a temporal scaler instance from this descriptor’s current property values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+

## Declaration

```swift
func makeTemporalScaler(device: any MTLDevice) -> (any MTLFXTemporalScaler)?
```

```objc
- (id<MTLFXTemporalScaler>) newTemporalScalerWithDevice:(id<MTLDevice>) device;
```

## Parameters

- `device`: An [`MTLDevice`](../../Metal/mtldevice.md) instance that represents the GPU that applies the temporal scaling effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/maketemporalscaler(device:))*