# colorTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var colorTextureUsage: MTLTextureUsage { get }
```

#### Discussion

The input texture you set to the [`colorTexture`](mtlfxspatialscaler/colortexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](https://developer.apple.com/documentation/Metal/MTLTextureUsage) options in this property.

## See Also

- [var colorTexture: (any MTLTexture)?](mtlfxspatialscaler/colortexture.md)
  An input color texture you set for the spatial scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](mtlfxspatialscaler/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentHeight: Int](mtlfxspatialscaler/inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler/colortextureusage)*