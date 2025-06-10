# ResamplingFilter

**Framework**: Accelerate  
**Kind**: typealias

A pointer to a resampling filter callback function.

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
typealias ResamplingFilter = UnsafeMutableRawPointer
```

#### Discussion

You pass a resampling filter callback to a shear function. The resampling filter pointer can point to a structure that contains a function, rows of precalculated values, flag settings, and so on. The shear function requires that the structure contains a scale factor.

## See Also

- [struct vImage_Buffer](vimage_buffer.md)
  An image buffer that stores an image’s pixel data, dimensions, and row stride.
- [typealias vImagePixelCount](vimagepixelcount.md)
  A type for the number of pixels.
- [struct vImage_AffineTransform](vimage_affinetransform.md)
  A structure for values that represent an affine transformation.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/resamplingfilter)*