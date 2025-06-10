# kvImageCopyInPlace

**Framework**: Accelerate  
**Kind**: var

A flag that copies the value of the edge pixel in the source to the destination.

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
var kvImageCopyInPlace: Int { get }
```

#### Discussion

When you set this flag, and a convolution function is processing an image pixel for which some of the kernel extends beyond the image boundaries, vImage does not compute the convolution. Instead, the value of the particular pixel unchanged; it’s simply copied to the destination image. This flag is valid only for convolution operations. The morphology functions do not use this flag because they do not use pixels outside the image in any of their calculations.

## See Also

- [var kvImageBackgroundColorFill: Int](kvimagebackgroundcolorfill.md)
  A flag that uses the background color for missing pixels.
- [var kvImageEdgeExtend: Int](kvimageedgeextend.md)
  A flag that extends the edges of the image infinitely.
- [var kvImageTruncateKernel: Int](kvimagetruncatekernel.md)
  A flag that uses only the part of the kernel that overlaps the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimagecopyinplace)*