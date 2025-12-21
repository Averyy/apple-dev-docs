# CVPixelFormatDescription

**Framework**: Core Video

An API that provides functions and types for defining custom pixel formats.

#### Overview

The Core Video pixel format description API defines functions and types for defining custom pixel formats. You should only use pixel format descriptions if you need to define a custom pixel format.

## Topics

### Creating Format Descriptions
- [func CVPixelFormatDescriptionCreateWithPixelFormatType(CFAllocator?, OSType) -> CFDictionary?](cvpixelformatdescriptioncreatewithpixelformattype(_:_:).md)
  Creates a pixel format description from a given `OSType` identifier.
- [func CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(CFDictionary, OSType)](cvpixelformatdescriptionregisterdescriptionwithpixelformattype(_:_:).md)
  Registers a pixel format description with Core Video.
### Retrieving Format Descriptions
- [func CVPixelFormatDescriptionArrayCreateWithAllPixelFormatTypes(CFAllocator?) -> CFArray?](cvpixelformatdescriptionarraycreatewithallpixelformattypes(_:).md)
  Returns all the pixel format descriptions known to Core Video.
### Data Types
- [struct CVFillExtendedPixelsCallBackData](cvfillextendedpixelscallbackdata.md)
  A structure for holding information that describes a custom extended pixel fill algorithm.
### Callbacks
- [typealias CVFillExtendedPixelsCallBack](cvfillextendedpixelscallback.md)
  Defines a pointer to a custom extended pixel-fill function, which is called whenever the system needs to pad a buffer holding your custom pixel format.
### Constants
- [Pixel Format Description Keys](pixel-format-description-keys.md)
  The attributes of a pixel format.
- [Pixel Format Identifiers](pixel-format-identifiers.md)
  Core Video does not provide support for all of these formats; this list defines only their names.

## See Also

- [CVBuffer](cvbuffer-nfm.md)
  An abstract base class that defines how to interact with data buffers.
- [CVImageBuffer](cvimagebuffer-q40.md)
  An interface for managing different types of image data.
- [CVPixelBuffer](cvpixelbuffer-q2e.md)
  An image buffer that holds pixels in main memory.
- [CVPixelBufferPool](cvpixelbufferpool-77o.md)
  A utility object for managing a recyclable set of pixel buffer objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescription)*