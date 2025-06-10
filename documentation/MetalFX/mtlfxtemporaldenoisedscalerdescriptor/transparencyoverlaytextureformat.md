# transparencyOverlayTextureFormat

**Framework**: MetalFX  
**Kind**: property

The pixel format of the input transparency overlay texture for the scaler you create with this descriptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- tvOS 18.0+

## Declaration

```swift
var transparencyOverlayTextureFormat: MTLPixelFormat { get set }
```

#### Discussion

You typically set this to a 4-channel RGBA texture format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/transparencyoverlaytextureformat)*