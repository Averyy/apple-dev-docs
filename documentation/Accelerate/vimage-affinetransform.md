# vImage_AffineTransform

**Framework**: Accelerate  
**Kind**: struct

A structure for values that represent an affine transformation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct vImage_AffineTransform
```

#### Overview

This structure represents the 3x2 matrix :

![3 by 2 matrix](https://docs-assets.developer.apple.com/published/15175700351555931d77e36e3b8efd15/media-2557524.gif)

In 32-bit applications, this structure is just like the Core Graphics [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) data structure. In 64-bit applications, the Core Graphics data structure is equivalent to [`vImage_AffineTransform_Double`](vimage_affinetransform_double.md). Most of the time, you should use the [`vImage_CGAffineTransform`](vimage_cgaffinetransform.md) data structure, which changes size depending on architecture.

The [`CGAffineTransform`](https://developer.apple.com/documentation/CoreGraphics/cgaffinetransform) describes functions for creating and manipulating matrixes of this form.

## Topics

### Initializers
- [init(a: Float, b: Float, c: Float, d: Float, tx: Float, ty: Float)](vimage_affinetransform/init(a:b:c:d:tx:ty:)-58fxt.md)
  Returns a new affine transform.
- [init()](vimage_affinetransform/init.md)
- [init(a: CGFloat, b: CGFloat, c: CGFloat, d: CGFloat, tx: CGFloat, ty: CGFloat)](vimage_affinetransform/init(a:b:c:d:tx:ty:)-6b4yl.md)
### Affine Transform Matrix Elements
- [var a: Float](vimage_affinetransform/a.md)
  The entry at position `[1,1]` in the matrix.
- [var b: Float](vimage_affinetransform/b.md)
  The entry at position `[1,2]` in the matrix.
- [var c: Float](vimage_affinetransform/c.md)
  The entry at position `[2,1]` in the matrix.
- [var d: Float](vimage_affinetransform/d.md)
  The entry at position `[2,2]` in the matrix.
- [var tx: Float](vimage_affinetransform/tx.md)
  The entry at position `[3,1]` in the matrix.
- [var ty: Float](vimage_affinetransform/ty.md)
  The entry at position `[3,2]` in the matrix.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct vImage_Buffer](vimage_buffer.md)
  An image buffer that stores an image’s pixel data, dimensions, and row stride.
- [typealias vImagePixelCount](vimagepixelcount.md)
  A type for the number of pixels.
- [struct vImage_AffineTransform_Double](vimage_affinetransform_double.md)
  A structure for values that represent a double-precision affine transformation.
- [typealias vImage_CGAffineTransform](vimage_cgaffinetransform.md)
  A structure for values that represent a Core Graphics–compatible affine transformation.
- [typealias vImage_Error](vimage_error.md)
  A type for image errors.
- [typealias vImage_Flags](vimage_flags.md)
  A type for processing options.
- [typealias GammaFunction](gammafunction.md)
  A type for a gamma function.
- [typealias ResamplingFilter](resamplingfilter.md)
  A pointer to a resampling filter callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_affinetransform)*