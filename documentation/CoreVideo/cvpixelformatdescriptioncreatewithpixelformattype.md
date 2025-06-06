# CVPixelFormatDescriptionCreateWithPixelFormatType(_:_:)

**Framework**: Core Video  
**Kind**: func

Creates a pixel format description from a given `OSType` identifier.

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
func CVPixelFormatDescriptionCreateWithPixelFormatType(_ allocator: CFAllocator?, _ pixelFormat: OSType) -> CFDictionary?
```

#### Return Value

A Core Foundation dictionary containing the pixel format description. See [`Pixel Format Description Keys`](pixel-format-description-keys.md) for a list of keys relevant to the format description.

## Parameters

- `allocator`: The allocator to use when creating the description. Pass   to specify the default allocator.
- `pixelFormat`: A four-character code that identifies the pixel format you want to obtain.

## See Also

- [func CVPixelFormatDescriptionRegisterDescriptionWithPixelFormatType(CFDictionary, OSType)](cvpixelformatdescriptionregisterdescriptionwithpixelformattype(_:_:).md)
  Registers a pixel format description with Core Video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelformatdescriptioncreatewithpixelformattype(_:_:))*