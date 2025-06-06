# Pixel Formats

**Framework**: Quartz

Supported image pixel formats.

## Topics

### Constants
- [let QCPlugInPixelFormatARGB8: String](qcpluginpixelformatargb8.md)
  An ARGB8 format. The alpha component is stored in the most significant bits of each pixel. Each pixel component is 8 bits. For best performance, use this format on PowerPC-based Macintosh computers, as it represents of the order of the data in memory.
- [let QCPlugInPixelFormatBGRA8: String](qcpluginpixelformatbgra8.md)
  A  BGRA8 format. The alpha component is stored in the least significant bits of each pixel. Each pixel component is 8 bits. For best performance, use this format on Intel-PC-based Macintosh computers, as it represents of the order of the data in memory.
- [let QCPlugInPixelFormatRGBAf: String](qcpluginpixelformatrgbaf.md)
  An RGBAf format. Pixel components are represented as floating-point values.
- [let QCPlugInPixelFormatI8: String](qcpluginpixelformati8.md)
  An I8 format. Intensity information is represented as an 8-bit value.
- [let QCPlugInPixelFormatIf: String](qcpluginpixelformatif.md)
  An If format. Intensity information is represented as a floating-point value.

## See Also

- [Patch Attributes](patch-attributes.md)
  Attributes for custom patches.
- [Input and Output Port Attributes](input-and-output-port-attributes.md)
  Attributes for input and output ports.
- [Port Input and Output Types](port-input-and-output-types.md)
  Data types for input and output ports.
- [Execution Arguments](execution-arguments.md)
  Arguments to the method [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md).
- [struct QCPlugInExecutionMode](qcpluginexecutionmode.md)
  Execution modes for custom patches.
- [struct QCPlugInTimeMode](qcplugintimemode.md)
  Time modes for custom patches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/pixel-formats)*