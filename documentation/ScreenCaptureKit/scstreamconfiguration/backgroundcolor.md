# backgroundColor

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A background color for the output.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
unowned(unsafe) var backgroundColor: CGColor { get set }
```

```objc
@property (nonatomic, assign) CGColorRef backgroundColor;
```

## See Also

### Configuring colors
- [var pixelFormat: OSType](./pixelformat.md)
  A pixel format for sample buffers that a stream outputs.
- [var colorMatrix: CFString](./colormatrix.md)
  A color matrix to apply to the output surface.
- [var colorSpaceName: CFString](./colorspacename.md)
  A color space to use for the output buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamconfiguration/backgroundcolor)*