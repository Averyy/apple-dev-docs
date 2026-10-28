# colorMatrix

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A color matrix to apply to the output surface.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
unowned(unsafe) var colorMatrix: CFString { get set }
```

```objc
@property (nonatomic, assign) CFStringRef colorMatrix;
```

## Discussion

You can specify a value for this property if your pixel format is `420v` or `420f`. The value must be one of the strings specified in [Display Stream YCbCr to RGB conversion Matrix Options](../../CoreGraphics/display-stream-ycbcr-to-rgb-conversion-matrix-options.md).

## See Also

### Configuring colors
- [var pixelFormat: OSType](./pixelformat.md)
  A pixel format for sample buffers that a stream outputs.
- [var colorSpaceName: CFString](./colorspacename.md)
  A color space to use for the output buffer.
- [var backgroundColor: CGColor](./backgroundcolor.md)
  A background color for the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/colormatrix)*