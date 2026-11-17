# colorTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The minimal texture usage options that your app’s input color texture must set to apply the spatial scaler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var colorTextureUsage: MTLTextureUsage { get }
```

```objc
@property (nonatomic, readonly) MTLTextureUsage colorTextureUsage;
```

## Discussion

The input texture you set to the [`colorTexture`](./colortexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options in this property.

## See Also

### Configuring the image input
- [var colorTexture: (any MTLTexture)?](./colortexture.md)
  An input color texture you set for the spatial scaler that supports the correct color texture usage options.
- [var inputContentWidth: Int](./inputcontentwidth.md)
  The width, in pixels, of the region within the color texture the spatial scaler uses as its input.
- [var inputContentHeight: Int](./inputcontentheight.md)
  The height, in pixels, of the region within the color texture the spatial scaler uses as its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase/colortextureusage)*