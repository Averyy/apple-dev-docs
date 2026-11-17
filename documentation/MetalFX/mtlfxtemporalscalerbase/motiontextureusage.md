# motionTextureUsage

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var motionTextureUsage: MTLTextureUsage { get }
```

```objc
@property (nonatomic, readonly) MTLTextureUsage motionTextureUsage;
```

## Discussion

The input texture you set to the [`motionTexture`](./motiontexture.md) property must use the same set (or a superset) of the [`MTLTextureUsage`](../../Metal/mtltextureusage.md) options in this property.

## See Also

### Configuring the motion input
- [var motionTexture: (any MTLTexture)?](./motiontexture.md)
  An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.
- [var motionVectorScaleX: Float](./motionvectorscalex.md)
  The horizontal scale factor the temporal scaler applies to the input motion texture.
- [var motionVectorScaleY: Float](./motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/motiontextureusage)*