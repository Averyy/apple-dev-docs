# Histogram

**Framework**: Accelerate

Calculate or manipulate an image’s histogram.

## Topics

### Performing contrast stretching
- [func vImageContrastStretch_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecontraststretch_planar8(_:_:_:).md)
  Performs contrast stretching on an 8-bit planar buffer.
- [func vImageContrastStretch_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagecontraststretch_planarf(_:_:_:_:_:_:_:).md)
  Performs contrast stretching on a 32-bit planar buffer.
- [func vImageContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecontraststretch_argb8888(_:_:_:).md)
  Performs contrast stretching on an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageContrastStretch_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagecontraststretch_argbffff(_:_:_:_:_:_:_:).md)
  Performs contrast stretching on a 32-bit-per-channel, 4-channel interleaved buffer.
### Performing ends-in contrast stretching
- [func vImageEndsInContrastStretch_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt32, UInt32, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_planar8(_:_:_:_:_:).md)
  Performs ends-in contrast stretching on an 8-bit planar buffer.
- [func vImageEndsInContrastStretch_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, UInt32, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_planarf(_:_:_:_:_:_:_:_:_:).md)
  Performs ends-in contrast stretching on a 32-bit planar buffer.
- [func vImageEndsInContrastStretch_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt32>, UnsafePointer<UInt32>, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_argb8888(_:_:_:_:_:).md)
  Performs ends-in contrast stretching on an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageEndsInContrastStretch_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<UInt32>, UnsafePointer<UInt32>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageendsincontraststretch_argbffff(_:_:_:_:_:_:_:_:_:).md)
  Performs ends-in contrast stretching on a 32-bit-per-channel, 4-channel interleaved buffer.
### Equalizing a histogram
- [func vImageEqualization_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageequalization_planar8(_:_:_:).md)
  Performs histogram equalization on an 8-bit planar buffer.
- [func vImageEqualization_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageequalization_planarf(_:_:_:_:_:_:_:).md)
  Performs histogram equalization on a 32-bit planar buffer.
- [func vImageEqualization_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageequalization_argb8888(_:_:_:).md)
  Performs histogram equalization on an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageEqualization_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageequalization_argbffff(_:_:_:_:_:_:_:).md)
  Performs histogram equalization on a 32-bit-per-channel, 4-channel interleaved buffer.
### Calculating a histogram
- [func vImageHistogramCalculation_Planar8(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_planar8(_:_:_:).md)
  Calculates the histogram of an 8-bit planar buffer.
- [func vImageHistogramCalculation_PlanarF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_planarf(_:_:_:_:_:_:).md)
  Calculates the histogram of a 32-bit planar buffer.
- [func vImageHistogramCalculation_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_argb8888(_:_:_:).md)
  Calculates the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramCalculation_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafeMutablePointer<vImagePixelCount>?>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramcalculation_argbffff(_:_:_:_:_:_:).md)
  Calculates the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.
### Specifying a histogram
- [func vImageHistogramSpecification_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImagePixelCount>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_planar8(_:_:_:_:).md)
  Specifies the histogram of an 8-bit planar buffer.
- [func vImageHistogramSpecification_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafePointer<vImagePixelCount>, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramspecification_planarf(_:_:_:_:_:_:_:_:).md)
  Specifies the histogram of a 32-bit planar buffer.
- [func vImageHistogramSpecification_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argb8888(_:_:_:_:).md)
  Specifies the histogram of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageHistogramSpecification_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<UnsafePointer<vImagePixelCount>?>!, UInt32, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimagehistogramspecification_argbffff(_:_:_:_:_:_:_:_:).md)
  Specifes the histogram of a 32-bit-per-channel, 4-channel interleaved buffer.

## See Also

- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Adjusting the hue of an image](adjusting-the-hue-of-an-image.md)
  Convert an image to L*a*b* color space and apply hue adjustment.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/histogram)*