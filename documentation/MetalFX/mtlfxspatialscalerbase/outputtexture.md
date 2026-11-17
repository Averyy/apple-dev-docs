# outputTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An output texture that supports the correct depth texture usage options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var outputTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> outputTexture;
```

## Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`storageMode`](../../Metal/mtlresource/storagemode.md) property is [`MTLStorageMode.private`](../../Metal/mtlstoragemode/private.md).
- The texture’s [`usage`](../../Metal/mtltexture/usage.md) property uses [`colorTextureUsage`](./colortextureusage.md) property’s [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options as a minimum, and can use additional options.
- The texture’s dimensions is equal to the [`outputWidth`](./outputwidth.md) and [`outputHeight`](./outputheight.md) properties.

## See Also

### Configuring the image output
- [var outputTextureUsage: MTLTextureUsage](./outputtextureusage.md)
  The minimal texture usage options that your app’s output texture must set to apply the spatial scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase/outputtexture)*