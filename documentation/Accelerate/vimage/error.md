# vImage.Error

**Framework**: Accelerate  
**Kind**: enum

An error that occurs during a vImage operation.

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
enum Error
```

## Topics

### Enumeration Cases
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
- [vImage.Error.invalidKernelSize](vimage/error/invalidkernelsize.md)
  An error indicating that either the kernel height, the kernel width, or both, are even.
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
- [vImage.Error.outOfPlaceOperationRequired](vimage/error/outofplaceoperationrequired.md)
  An error indicating that the source images and destination images alias the same image data, but must not.
- [vImage.Error.roiLargerThanInputBuffer](vimage/error/roilargerthaninputbuffer.md)
  An error indicating that the region of interest extends beyond the bottom edge or right edge of the source buffer.
- [vImage.Error.unknownFlagsBit](vimage/error/unknownflagsbit.md)
  An error indicating that a bit in the flags field isn’t supported.
- [vImage.Error.unsupportedConversion](vimage/error/unsupportedconversion.md)
  An error indicating that the requested conversion isn’t supported.
### Initializers
- [init(vImageError: vImage_Error)](vimage/error/init(vimageerror:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [vImage.BlendMode](vimage/blendmode.md)
  Constants that specify an alpha blending mode.
- [vImage.BufferType](vimage/buffertype.md)
  Codes that represent vImage buffer types.
- [vImage.ChannelOrdering](vimage/channelordering.md)
  Constants that specify the channel ordering of a pixel buffer.
- [vImage.CompositeMode](vimage/compositemode.md)
  Constants that specify whether the format of layers is premultiplied or nonpremultiplied.
- [vImage.EdgeMode](vimage/edgemode.md)
  Constants that specify edge modes for convolution operations.
- [vImage.FloodFillConnectivity](vimage/floodfillconnectivity.md)
- [vImage.Gamma](vimage/gamma.md)
  Describes either a used-defined or constant gamma.
- [vImage.MorphologyOperation](vimage/morphologyoperation.md)
  Describes which morphology operation to perform.
- [vImage.ReflectionAxis](vimage/reflectionaxis.md)
  The axis to reflect an image.
- [vImage.Rotation](vimage/rotation.md)
  The angle to rotate an image.
- [vImage.ShearDirection](vimage/sheardirection.md)
  The shear direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/error)*