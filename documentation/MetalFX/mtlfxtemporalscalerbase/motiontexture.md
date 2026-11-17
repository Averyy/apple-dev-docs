# motionTexture

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var motionTexture: (any MTLTexture)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLTexture> motionTexture;
```

## Discussion

The texture you set to this property must meet the following requirements:

- The texture’s [`usage`](../../Metal/mtltexture/usage.md) property must use the same [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options as (or be a superset of) the temporal scaling effect’s [`motionTextureUsage`](./motiontextureusage.md) property.
- The texture’s dimensions must be equal to the [`inputWidth`](./inputwidth.md) and [`inputHeight`](./inputheight.md) properties.

## See Also

### Configuring the motion input
- [var motionTextureUsage: MTLTextureUsage](./motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.
- [var motionVectorScaleX: Float](./motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](./motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/motiontexture)*