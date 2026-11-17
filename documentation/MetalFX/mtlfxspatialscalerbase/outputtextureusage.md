# outputTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The minimal texture usage options that your app’s output texture must set to apply the spatial scaler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var outputTextureUsage: MTLTextureUsage { get }
```

```objc
@property (nonatomic, readonly) MTLTextureUsage outputTextureUsage;
```

## Discussion

The texture your app sets to the [`outputTexture`](./outputtexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options in this property.

## See Also

### Configuring the image output
- [var outputTexture: (any MTLTexture)?](./outputtexture.md)
  An output texture that supports the correct depth texture usage options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase/outputtextureusage)*