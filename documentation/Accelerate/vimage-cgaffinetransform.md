# vImage_CGAffineTransform

**Framework**: Accelerate  
**Kind**: typealias

A structure for values that represent a Core Graphics–compatible affine transformation.

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
typealias vImage_CGAffineTransform = vImage_AffineTransform_Double
```

## Mentions

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)

#### Discussion

This structure represents the 3x2 matrix :

![3 by 2 matrix](https://docs-assets.developer.apple.com/published/15175700351555931d77e36e3b8efd15/media-2557524.gif)

This structure changes size to be the same size as the Core Graphics [`CGAffineTransform`](https://developer.apple.com/documentation/CoreFoundation/CGAffineTransform) data structure. [`CGAffineTransform`](https://developer.apple.com/documentation/CoreGraphics/cgaffinetransform) describes functions for creating and manipulating matrixes of this form.

## See Also

- [struct vImage_Buffer](vimage_buffer.md)
  An image buffer that stores an image’s pixel data, dimensions, and row stride.
- [typealias vImagePixelCount](vimagepixelcount.md)
  A type for the number of pixels.
- [struct vImage_AffineTransform](vimage_affinetransform.md)
  A structure for values that represent an affine transformation.
- [struct vImage_AffineTransform_Double](vimage_affinetransform_double.md)
  A structure for values that represent a double-precision affine transformation.
- [typealias vImage_Error](vimage_error.md)
  A type for image errors.
- [typealias vImage_Flags](vimage_flags.md)
  A type for processing options.
- [typealias GammaFunction](gammafunction.md)
  A type for a gamma function.
- [typealias ResamplingFilter](resamplingfilter.md)
  A pointer to a resampling filter callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgaffinetransform)*