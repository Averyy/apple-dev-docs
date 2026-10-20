# colorTextureFormat

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

The pixel format of the input color texture for the spatial scaler you create with this descriptor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+
- visionOS 1.0+

## Declaration

```swift
var colorTextureFormat: MTLPixelFormat { get set }
```

```objc
@property (nonatomic, readwrite) MTLPixelFormat colorTextureFormat;
```

## See Also

### Configuring a spatial scaler’s input
- [var inputWidth: Int](./inputwidth.md)
  The width of the input color texture for the spatial scaler you create with this descriptor.
- [var inputHeight: Int](./inputheight.md)
  The height of the input color texture for the spatial scaler you create with this descriptor.
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](./colorprocessingmode.md)
  The color space of the input color texture for the spatial scaler you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/colortextureformat)*