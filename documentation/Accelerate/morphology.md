# Morphology

**Framework**: Accelerate  
**Role**: API Collection

Dilate and erode images.

## Topics

### Dilating an object
- [func vImageDilate_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagedilate_planar8%28_,_,_,_,_,_,_,_%29.md)
  Dilates an 8-bit planar buffer.
- [func vImageDilate_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagedilate_planarf%28_,_,_,_,_,_,_,_%29.md)
  Dilates a 32-bit planar buffer.
- [func vImageDilate_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagedilate_argb8888%28_,_,_,_,_,_,_,_%29.md)
  Dilates an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageDilate_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagedilate_argbffff%28_,_,_,_,_,_,_,_%29.md)
  Dilates a 32-bit-per-channel, 4-channel interleaved buffer.
### Eroding an object
- [func vImageErode_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimageerode_planar8%28_,_,_,_,_,_,_,_%29.md)
  Erodes an 8-bit planar buffer.
- [func vImageErode_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimageerode_planarf%28_,_,_,_,_,_,_,_%29.md)
  Erodes a 32-bit planar buffer.
- [func vImageErode_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimageerode_argb8888%28_,_,_,_,_,_,_,_%29.md)
  Erodes an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageErode_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimageerode_argbffff%28_,_,_,_,_,_,_,_%29.md)
  Erodes a 32-bit-per-channel, 4-channel interleaved buffer.
### Maximizing an object
- [func vImageMax_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemax_planar8%28_,_,_,_,_,_,_,_%29.md)
  Maximizes an 8-bit planar buffer.
- [func vImageMax_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemax_planarf%28_,_,_,_,_,_,_,_%29.md)
  Maximizes a 32-bit planar buffer.
- [func vImageMax_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemax_argb8888%28_,_,_,_,_,_,_,_%29.md)
  Maximizes an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageMax_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemax_argbffff%28_,_,_,_,_,_,_,_%29.md)
  Maximizes a 32-bit-per-channel, 4-channel interleaved buffer.
### Minimizing an object
- [func vImageMin_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemin_planar8%28_,_,_,_,_,_,_,_%29.md)
  Minimizes an 8-bit planar buffer.
- [func vImageMin_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemin_planarf%28_,_,_,_,_,_,_,_%29.md)
  Minimizes a 32-bit planar buffer.
- [func vImageMin_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemin_argb8888%28_,_,_,_,_,_,_,_%29.md)
  Minimizes an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageMin_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](./vimagemin_argbffff%28_,_,_,_,_,_,_,_%29.md)
  Minimizes an 8-bit-per-channel, 4-channel interleaved buffer.

## See Also

### Convolution and Morphology
- [Blurring an image](./blurring-an-image.md)
  Filter an image by convolving it with custom and high-speed kernels.
- [Adding a bokeh effect to images](./adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [Convolution](./convolution.md)
  Apply a convolution kernel to an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/morphology)*