# colorSpaceName

**Framework**: ScreenCaptureKit  
**Kind**: property

A color space to use for the output buffer.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
unowned(unsafe) var colorSpaceName: CFString { get set }
```

#### Discussion

If you don’t specify a value, the output buffer uses the same color space as the display. If you specify a value, if must be one of the strings specified in [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace).

## See Also

- [var pixelFormat: OSType](scstreamconfiguration/pixelformat.md)
  A pixel format for sample buffers that a stream outputs.
- [var colorMatrix: CFString](scstreamconfiguration/colormatrix.md)
  A color matrix to apply to the output surface.
- [var backgroundColor: CGColor](scstreamconfiguration/backgroundcolor.md)
  A background color for the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/colorspacename)*