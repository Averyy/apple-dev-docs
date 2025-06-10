# kvImageUnknownFlagsBit

**Framework**: Accelerate  
**Kind**: var

The flag is not recognized.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kvImageUnknownFlagsBit: Int { get }
```

## See Also

- [vImage.Error](vimage/error.md)
  An error that occurs during a vImage operation.
- [var kvImageNoError: Int](kvimagenoerror.md)
  The vImage function completed without error.
- [var kvImageRoiLargerThanInputBuffer: Int](kvimageroilargerthaninputbuffer.md)
  The region of interest, as specified by the `srcOffsetToROI_X` and `srcOffsetToROI_Y` parameters and the height and width of the destination buffer, extends beyond the bottom edge or right edge of the source buffer.
- [var kvImageInvalidKernelSize: Int](kvimageinvalidkernelsize.md)
  Either the kernel height, the kernel width, or both, are even.
- [var kvImageInvalidEdgeStyle: Int](kvimageinvalidedgestyle.md)
  The edge style specified is invalid.
- [var kvImageInvalidOffset_X: Int](kvimageinvalidoffset_x.md)
  The `srcOffsetToROI_X` parameter that specifies the left edge of the region of interest is greater than the width of the source image.
- [var kvImageInvalidOffset_Y: Int](kvimageinvalidoffset_y.md)
  The `srcOffsetToROI_Y` parameter that specifies the top edge of the region of interest is greater than the height of the source image.
- [var kvImageMemoryAllocationError: Int](kvimagememoryallocationerror.md)
  An attempt to allocate memory failed.
- [var kvImageNullPointerArgument: Int](kvimagenullpointerargument.md)
  A pointer parameter is `NULL` and it must not be.
- [var kvImageInvalidParameter: Int](kvimageinvalidparameter.md)
  Invalid parameter.
- [var kvImageBufferSizeMismatch: Int](kvimagebuffersizemismatch.md)
  The function requires the source and destination buffers to have the same height and the same width, but they do not.
- [var kvImageColorSyncIsAbsent: Int](kvimagecolorsyncisabsent.md)
- [var kvImageCoreVideoIsAbsent: Int](kvimagecorevideoisabsent.md)
- [var kvImageInternalError: Int](kvimageinternalerror.md)
  A serious error occured inside vImage, which prevented vImage from continuing.
- [var kvImageInvalidCVImageFormat: Int](kvimageinvalidcvimageformat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimageunknownflagsbit)*