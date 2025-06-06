# inputContentHeight

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The height, in pixels, of the region within the color texture the spatial scaler uses as its input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var inputContentHeight: Int { get set }
```

#### Discussion

The input content height must be less than or equal to [`inputHeight`](mtlfxspatialscaler/inputheight.md).

## See Also

- [var colorTextureUsage: MTLTextureUsage](mtlfxspatialscaler/colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.
- [var colorTexture: (any MTLTexture)?](mtlfxspatialscaler/colortexture.md)
  An input color texture you set for the spatial scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](mtlfxspatialscaler/inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler/inputcontentheight)*