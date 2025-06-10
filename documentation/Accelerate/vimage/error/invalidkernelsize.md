# vImage.Error.invalidKernelSize

**Framework**: Accelerate  
**Kind**: case

An error indicating that either the kernel height, the kernel width, or both, are even.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
case invalidKernelSize
```

## See Also

- [vImage.Error.bufferSizeMismatch](vimage/error/buffersizemismatch.md)
  An error indicating that the function requires the source and destination buffers to have the same size, but they don’t.
- [vImage.Error.colorSyncIsAbsent](vimage/error/colorsyncisabsent.md)
  An error indicating that the ColorSync framework is missing.
- [vImage.Error.coreVideoIsAbsent](vimage/error/corevideoisabsent.md)
  An error indicating that the Core Video framework is missing.
- [vImage.Error.internalError](vimage/error/internalerror.md)
  A serious error occurred inside vImage, which prevented vImage from continuing.
- [vImage.Error.invalidCVImageFormat](vimage/error/invalidcvimageformat.md)
  An error indicating that a Core Video format is invalid.
- [vImage.Error.invalidEdgeStyle](vimage/error/invalidedgestyle.md)
  An error indicating that the specified edge style is invalid.
- [vImage.Error.invalidImageFormat](vimage/error/invalidimageformat.md)
  An error indicating that a specified Core Graphics or Core Video format is invalid.
- [vImage.Error.invalidImageObject](vimage/error/invalidimageobject.md)
  An error indicating that a specified Core Graphics image or Core Video pixel buffer is invalid.
- [vImage.Error.invalidOffset_X](vimage/error/invalidoffset_x.md)
  An error indicating that the parameter that specifies the left edge of the region of interest is greater than the width of the source image.
- [vImage.Error.invalidOffset_Y](vimage/error/invalidoffset_y.md)
  An error indicating that the parameter that specifies the top edge of the region of interest is greater than the height of the source image.
- [vImage.Error.invalidParameter](vimage/error/invalidparameter.md)
  An error indicating that a function parameter has an invalid value.
- [vImage.Error.invalidRowBytes](vimage/error/invalidrowbytes.md)
  An error indicating that the buffer’s row bytes field is invalid.
- [vImage.Error.memoryAllocationError](vimage/error/memoryallocationerror.md)
  An error indicating that an attempt to allocate memory failed.
- [vImage.Error.noError](vimage/error/noerror.md)
  The vImage function completed without error.
- [vImage.Error.nullPointerArgument](vimage/error/nullpointerargument.md)
  An error indicating that a pointer parameter is `NULL` and it must not be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/error/invalidkernelsize)*