# inputWidth

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property

The width of the input color texture for the spatial scaler you create with this descriptor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+
- visionOS 1.0+

## Declaration

```swift
var inputWidth: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger inputWidth;
```

## See Also

### Configuring a spatial scaler’s input
- [var inputHeight: Int](./inputheight.md)
  The height of the input color texture for the spatial scaler you create with this descriptor.
- [var colorTextureFormat: MTLPixelFormat](./colortextureformat.md)
  The pixel format of the input color texture for the spatial scaler you create with this descriptor.
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](./colorprocessingmode.md)
  The color space of the input color texture for the spatial scaler you create with this descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/inputwidth)*