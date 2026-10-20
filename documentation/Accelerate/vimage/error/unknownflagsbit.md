# vImage.Error.unknownFlagsBit

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

An error indicating that a bit in the flags field isn’t supported.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
case unknownFlagsBit
```

## See Also

### Enumeration Cases
- [vImage.Error.bufferSizeMismatch](./buffersizemismatch.md)
  An error indicating that the function requires the source and destination buffers to have the same size, but they don’t.
- [vImage.Error.colorSyncIsAbsent](./colorsyncisabsent.md)
  An error indicating that the ColorSync framework is missing.
- [vImage.Error.coreVideoIsAbsent](./corevideoisabsent.md)
  An error indicating that the Core Video framework is missing.
- [vImage.Error.internalError](./internalerror.md)
  A serious error occurred inside vImage, which prevented vImage from continuing.
- [vImage.Error.invalidCVImageFormat](./invalidcvimageformat.md)
  An error indicating that a Core Video format is invalid.
- [vImage.Error.invalidEdgeStyle](./invalidedgestyle.md)
  An error indicating that the specified edge style is invalid.
- [vImage.Error.invalidImageFormat](./invalidimageformat.md)
  An error indicating that a specified Core Graphics or Core Video format is invalid.
- [vImage.Error.invalidImageObject](./invalidimageobject.md)
  An error indicating that a specified Core Graphics image or Core Video pixel buffer is invalid.
- [vImage.Error.invalidKernelSize](./invalidkernelsize.md)
  An error indicating that either the kernel height, the kernel width, or both, are even.
- [vImage.Error.invalidOffset_X](./invalidoffset_x.md)
  An error indicating that the parameter that specifies the left edge of the region of interest is greater than the width of the source image.
- [vImage.Error.invalidOffset_Y](./invalidoffset_y.md)
  An error indicating that the parameter that specifies the top edge of the region of interest is greater than the height of the source image.
- [vImage.Error.invalidParameter](./invalidparameter.md)
  An error indicating that a function parameter has an invalid value.
- [vImage.Error.invalidRowBytes](./invalidrowbytes.md)
  An error indicating that the buffer’s row bytes field is invalid.
- [vImage.Error.memoryAllocationError](./memoryallocationerror.md)
  An error indicating that an attempt to allocate memory failed.
- [vImage.Error.noError](./noerror.md)
  The vImage function completed without error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/error/unknownflagsbit)*