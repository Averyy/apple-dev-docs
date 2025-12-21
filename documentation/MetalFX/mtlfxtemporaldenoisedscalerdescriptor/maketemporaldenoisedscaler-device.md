# makeTemporalDenoisedScaler(device:)

**Framework**: MetalFX  
**Kind**: method

Creates a denoiser scaler instance for a Metal device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- tvOS 18.0+

## Declaration

```swift
func makeTemporalDenoisedScaler(device: any MTLDevice) -> (any MTLFXTemporalDenoisedScaler)?
```

#### Return Value

 A denoiser scaler instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the denoiser scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/maketemporaldenoisedscaler(device:))*