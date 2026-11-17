# inputWidth

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The width, in pixels, of the input color texture for the spatial scaler.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.2+
- visionOS 1.0+

## Declaration

```swift
var inputWidth: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger inputWidth;
```

## See Also

### Inspecting the fixed settings
- [var inputHeight: Int](./inputheight.md)
  The height, in pixels, of the input color texture for the spatial scaler.
- [var colorTextureFormat: MTLPixelFormat](./colortextureformat.md)
  The pixel format of the input color texture for the spatial scaler.
- [var colorProcessingMode: MTLFXSpatialScalerColorProcessingMode](./colorprocessingmode.md)
  Reflects the color processing mode you set in this spatial scaler’s descriptor.
- [var outputWidth: Int](./outputwidth.md)
  The width, in pixels, of the output color texture for the spatial scaler.
- [var outputHeight: Int](./outputheight.md)
  The height, in pixels, of the output color texture for the spatial scaler.
- [var outputTextureFormat: MTLPixelFormat](./outputtextureformat.md)
  The pixel format of the output color texture for the spatial scaler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerbase/inputwidth)*