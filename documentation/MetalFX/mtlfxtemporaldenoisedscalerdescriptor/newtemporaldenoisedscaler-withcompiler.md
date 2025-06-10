# newTemporalDenoisedScaler(with:compiler:)

**Framework**: MetalFX  
**Kind**: method

Creates a denoiser scaler instance for a Metal device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- tvOS 18.0+

## Declaration

```swift
func newTemporalDenoisedScaler(with device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXTemporalDenoisedScaler)?
```

#### Return Value

 A denoiser scaler instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the denoiser scaler.
- `compiler`: A compiler instance this method can use to build pipeline state objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/newtemporaldenoisedscaler(with:compiler:))*