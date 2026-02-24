# pixelFormat

**Framework**: ScreenCaptureKit  
**Kind**: property

A pixel format for sample buffers that a stream outputs.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var pixelFormat: OSType { get set }
```

#### Discussion

A stream supports the following pixel formats:

- **`BGRA`**: Packed little endian ARGB8888.
- **`l10r`**: Packed little endian ARGB2101010.
- **`420v`**: Two-plane “video” range YCbCr 4:2:0.
- **`420f`**: Two-plane “full” range YCbCr 4:2:0.

## See Also

- [var colorMatrix: CFString](scstreamconfiguration/colormatrix.md)
  A color matrix to apply to the output surface.
- [var colorSpaceName: CFString](scstreamconfiguration/colorspacename.md)
  A color space to use for the output buffer.
- [var backgroundColor: CGColor](scstreamconfiguration/backgroundcolor.md)
  A background color for the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/pixelformat)*