# denoiseStrengthMaskTextureFormat

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

The pixel format of the input denoise strength mask texture for the scaler you create with this descriptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
var denoiseStrengthMaskTextureFormat: MTLPixelFormat { get set }
```

```objc
@property (nonatomic, readwrite) MTLPixelFormat denoiseStrengthMaskTextureFormat;
```

#### Discussion

You typically set this to a single-channel texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/denoisestrengthmasktextureformat)*