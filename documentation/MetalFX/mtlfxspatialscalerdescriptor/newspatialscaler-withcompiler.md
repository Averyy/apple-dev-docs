# newSpatialScaler(with:compiler:)

**Framework**: MetalFX  
**Kind**: method

Creates a spatial scaler instance for a Metal device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func newSpatialScaler(with device: any MTLDevice, compiler: any MTL4Compiler) -> (any MTL4FXSpatialScaler)?
```

#### Return Value

 A new spatial scaler instance upon success, or `nil` otherwise.

## Parameters

- `device`: The Metal device that creates the spatial scaler.
- `compiler`: A compiler instance this method can use to build pipeline state objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/newspatialscaler(with:compiler:))*