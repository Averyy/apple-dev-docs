# CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(_:_:)

**Framework**: Core Video  
**Kind**: func

Registers a pixel format description with Core Video.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(_ description: CFDictionary, _ pixelFormat: OSType)
```

#### Discussion

If you are using a custom pixel format, you must register the format with Core Video using this function. See [`Technical Q&A 1401: Registering Custom Pixel Formats with QuickTime and Core Video`](https://developer.apple.comhttp://developer.apple.com/qa/qa2005/qa1401.html) for more details.

## Parameters

- `description`: A Core Foundation dictionary containing the pixel format description. See   for a list of required and optional keys.
- `pixelFormat`: The four-character code (type  ) identifier for this pixel format.

## See Also

- [Core Video Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreVideo/CVProg_Intro/CVProg_Intro.html#//apple_ref/doc/uid/TP40001536)
- [func CVPixelFormatDescriptionCreateWithPixelFormatType(CFAllocator?, OSType) -> CFDictionary?](cvpixelformatdescriptioncreatewithpixelformattype(_:_:).md)
  Creates a pixel format description from a given `OSType` identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescriptionregisterdescriptionwithpixelformattype(_:_:))*