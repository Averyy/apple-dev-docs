# colorTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An input color texture you set for the spatial scaler that supports the correct color texture usage options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var colorTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> colorTexture;
```

## Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](../../Metal/mtltexture/usage.md) property must use the same [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options as (or be a superset of) the spatial scaling effect’s [`colorTextureUsage`](./colortextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](./inputwidth.md) and [`inputHeight`](./inputheight.md) properties.

## See Also

### Configuring the image input
- [var colorTextureUsage: MTLTextureUsage](./colortextureusage.md)
  The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.
- [var inputContentWidth: Int](./inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentHeight: Int](./inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase/colortexture)*