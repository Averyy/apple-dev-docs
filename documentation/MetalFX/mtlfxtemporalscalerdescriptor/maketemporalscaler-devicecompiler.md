# makeTemporalScaler(device:compiler:)

**Framework**: MetalFX  
**Kind**: method

Creates a temporal scaler instance for a Metal device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func makeTemporalScaler(device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXTemporalScaler)?
```

#### Return Value

 A new temporal scaler instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the temporal scaler.
- `compiler`: A compiler instance this method can use to build pipeline state objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/maketemporalscaler(device:compiler:))*