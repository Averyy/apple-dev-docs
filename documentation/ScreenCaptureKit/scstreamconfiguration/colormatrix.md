# colorMatrix

**Framework**: ScreenCaptureKit  
**Kind**: property

A color matrix to apply to the output surface.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
unowned(unsafe) var colorMatrix: CFString { get set }
```

#### Discussion

You can specify a value for this property if your pixel format is `420v` or `420f`. The value must be one of the strings specified in [`Display Stream YCbCr to RGB conversion Matrix Options`](https://developer.apple.com/documentation/CoreGraphics/display-stream-ycbcr-to-rgb-conversion-matrix-options).

## See Also

- [var pixelFormat: OSType](scstreamconfiguration/pixelformat.md)
  A pixel format for sample buffers that a stream outputs.
- [var colorSpaceName: CFString](scstreamconfiguration/colorspacename.md)
  A color space to use for the output buffer.
- [var backgroundColor: CGColor](scstreamconfiguration/backgroundcolor.md)
  A background color for the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/colormatrix)*