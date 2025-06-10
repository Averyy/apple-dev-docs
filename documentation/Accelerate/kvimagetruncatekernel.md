# kvImageTruncateKernel

**Framework**: Accelerate  
**Kind**: var

A flag that uses only the part of the kernel that overlaps the image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kvImageTruncateKernel: Int { get }
```

#### Discussion

This flag is valid only for convolution operations. When you set this flag, vImage restricts calculations to the portion of the kernel overlapping the image. It corrects the calculated pixel by first multiplying by the sum of all the kernel elements, then dividing by the sum of the kernel elements that are actually used. This preserves image brightness at the edges.

For integer kernels:

```objc
real_divisor = divisor * (sum of used kernel elements) / (sum of kernel elements)
```

The morphology functions do not use this flag because they do not use pixels outside the image in any of their calculations.

Kernel truncation is not robust for certain kernels. It can fail when any rectangular segment of the kernel that includes the center, and at least one of the corners, sums to zero. You typically see this with emboss or edge detection filters, or other filters that are designed to find the slope of a signal. For those kinds of filters, you should use the [`kvImageEdgeExtend`](kvimageedgeextend.md) option instead.

## See Also

- [var kvImageCopyInPlace: Int](kvimagecopyinplace.md)
  A flag that copies the value of the edge pixel in the source to the destination.
- [var kvImageBackgroundColorFill: Int](kvimagebackgroundcolorfill.md)
  A flag that uses the background color for missing pixels.
- [var kvImageEdgeExtend: Int](kvimageedgeextend.md)
  A flag that extends the edges of the image infinitely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/kvimagetruncatekernel)*