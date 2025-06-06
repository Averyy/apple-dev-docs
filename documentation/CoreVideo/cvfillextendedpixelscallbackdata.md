# CVFillExtendedPixelsCallBackData

**Framework**: Core Video  
**Kind**: struct

A structure for holding information that describes a custom extended pixel fill algorithm.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CVFillExtendedPixelsCallBackData
```

#### Overview

You must fill out this structure and store it as part of your pixel format description Core Foundation dictionary (key: `kCVPixelFormatFillExtendedPixelsCallback`, type: `CFData`). However, if your custom pixel format never needs the functionality of [`CVPixelBufferFillExtendedPixels(_:)`](cvpixelbufferfillextendedpixels(_:).md), you don’t need to add this key or implement the associated callback.

For more information about defining a custom pixel format, see [`Pixel Format Description Keys`](pixel-format-description-keys.md).

## Topics

### Initializers
- [init()](cvfillextendedpixelscallbackdata/init.md)
- [init(version: CFIndex, fillCallBack: CVFillExtendedPixelsCallBack?, refCon: UnsafeMutableRawPointer?)](cvfillextendedpixelscallbackdata/init(version:fillcallback:refcon:).md)
### Properties
- [var fillCallBack: CVFillExtendedPixelsCallBack?](cvfillextendedpixelscallbackdata/fillcallback.md)
- [var refCon: UnsafeMutableRawPointer?](cvfillextendedpixelscallbackdata/refcon.md)
  A pointer to application-defined data that is passed to your custom pixel fill function.
- [var version: CFIndex](cvfillextendedpixelscallbackdata/version.md)
  The version of this fill algorithm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvfillextendedpixelscallbackdata)*