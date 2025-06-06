# colorTexture

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

An input color texture you set for the spatial scaler that supports the correct color texture usage options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var colorTexture: (any MTLTexture)? { get set }
```

#### Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](https://developer.apple.com/documentation/Metal/MTLTexture/usage) property must use the same [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options as (or be a superset of) the spatial scaling effect’s [`colorTextureUsage`](mtlfxspatialscaler/colortextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](mtlfxspatialscaler/inputwidth.md) and [`inputHeight`](mtlfxspatialscaler/inputheight.md) properties.

## See Also

- [var colorTextureUsage: MTLTextureUsage](mtlfxspatialscaler/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.
- [var inputContentWidth: Int](mtlfxspatialscaler/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentHeight: Int](mtlfxspatialscaler/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler/colortexture)*