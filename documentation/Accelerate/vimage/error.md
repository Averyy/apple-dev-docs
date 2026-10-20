# vImage.Error

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

An error that occurs during a vImage operation.

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
enum Error
```

## Topics

### Enumeration Cases
- [vImage.Error.bufferSizeMismatch](./error/buffersizemismatch.md)
  An error indicating that the function requires the source and destination buffers to have the same size, but they don’t.
- [vImage.Error.colorSyncIsAbsent](./error/colorsyncisabsent.md)
  An error indicating that the ColorSync framework is missing.
- [vImage.Error.coreVideoIsAbsent](./error/corevideoisabsent.md)
  An error indicating that the Core Video framework is missing.
- [vImage.Error.internalError](./error/internalerror.md)
  A serious error occurred inside vImage, which prevented vImage from continuing.
- [vImage.Error.invalidCVImageFormat](./error/invalidcvimageformat.md)
  An error indicating that a Core Video format is invalid.
- [vImage.Error.invalidEdgeStyle](./error/invalidedgestyle.md)
  An error indicating that the specified edge style is invalid.
- [vImage.Error.invalidImageFormat](./error/invalidimageformat.md)
  An error indicating that a specified Core Graphics or Core Video format is invalid.
- [vImage.Error.invalidImageObject](./error/invalidimageobject.md)
  An error indicating that a specified Core Graphics image or Core Video pixel buffer is invalid.
- [vImage.Error.invalidKernelSize](./error/invalidkernelsize.md)
  An error indicating that either the kernel height, the kernel width, or both, are even.
- [vImage.Error.invalidOffset_X](./error/invalidoffset_x.md)
  An error indicating that the parameter that specifies the left edge of the region of interest is greater than the width of the source image.
- [vImage.Error.invalidOffset_Y](./error/invalidoffset_y.md)
  An error indicating that the parameter that specifies the top edge of the region of interest is greater than the height of the source image.
- [vImage.Error.invalidParameter](./error/invalidparameter.md)
  An error indicating that a function parameter has an invalid value.
- [vImage.Error.invalidRowBytes](./error/invalidrowbytes.md)
  An error indicating that the buffer’s row bytes field is invalid.
- [vImage.Error.memoryAllocationError](./error/memoryallocationerror.md)
  An error indicating that an attempt to allocate memory failed.
- [vImage.Error.noError](./error/noerror.md)
  The vImage function completed without error.
- [vImage.Error.nullPointerArgument](./error/nullpointerargument.md)
  An error indicating that a pointer parameter is `NULL` and it must not be.
- [vImage.Error.outOfPlaceOperationRequired](./error/outofplaceoperationrequired.md)
  An error indicating that the source images and destination images alias the same image data, but must not.
- [vImage.Error.roiLargerThanInputBuffer](./error/roilargerthaninputbuffer.md)
  An error indicating that the region of interest extends beyond the bottom edge or right edge of the source buffer.
- [vImage.Error.unknownFlagsBit](./error/unknownflagsbit.md)
  An error indicating that a bit in the flags field isn’t supported.
- [vImage.Error.unsupportedConversion](./error/unsupportedconversion.md)
  An error indicating that the requested conversion isn’t supported.
### Initializers
- [init(vImageError: vImage_Error)](./error/init%28vimageerror%29.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [vImage.BlendMode](./blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](./buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](./channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](./compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](./edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.FloodFillConnectivity](./floodfillconnectivity.md)
- [vImage.Gamma](./gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.MorphologyOperation](./morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](./reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](./rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](./sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/error)*