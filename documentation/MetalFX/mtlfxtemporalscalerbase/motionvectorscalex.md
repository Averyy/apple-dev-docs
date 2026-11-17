# motionVectorScaleX

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The horizontal scale factor the temporal scaler applies to the input motion texture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var motionVectorScaleX: Float { get set }
```

```objc
@property (nonatomic) float motionVectorScaleX;
```

## Discussion

The scaler converts the horizontal component of each value in [`motionTexture`](./motiontexture.md) into fragment (pixel) coordinates by multiplying it by this property’s value.

## See Also

### Configuring the motion input
- [var motionTextureUsage: MTLTextureUsage](./motiontextureusage.md)
  The minimal texture usage options that your app’s input motion texture must set to apply the temporal scaler.
- [var motionTexture: (any MTLTexture)?](./motiontexture.md)
  An input motion texture you set for the temporal scaler that supports the correct motion texture usage options.
- [var motionVectorScaleY: Float](./motionvectorscaley.md)
  The vertical scale factor the temporal scaler applies to the input motion texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerbase/motionvectorscalex)*