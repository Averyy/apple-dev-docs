# Alpha compositing

**Framework**: Accelerate

Composite images together.

## Topics

### Performing nonpremultiplied alpha compositing
- [func vImageAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_planar8(_:_:_:_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit planar buffers.
- [func vImageAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_planarf(_:_:_:_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit planar buffers.
- [func vImageAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_argb8888(_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 8-bit-per-channel, 4-channel ARGB buffers.
- [func vImageAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_argbffff(_:_:_:_:).md)
  Performs nonpremultiplied alpha compositing of two 32-bit-per-channel, 4-channel ARGB buffers.
### Performing premultiplied alpha compositing
- [func vImagePremultipliedAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_planar8(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit planar buffers.
- [func vImagePremultipliedAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_planarf(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit planar buffers.
- [func vImagePremultipliedAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_argb8888(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel ARGB buffers.
- [func vImagePremultipliedAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_argbffff(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel ARGB buffers.
- [func vImagePremultipliedAlphaBlend_BGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_bgra8888(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers.
- [func vImagePremultipliedAlphaBlend_BGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablend_bgraffff(_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel BGRA buffers.
### Performing premultiplied alpha compositing with blend modes
- [func vImagePremultipliedAlphaBlendLighten_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendlighten_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the lighten blend mode.
- [func vImagePremultipliedAlphaBlendDarken_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablenddarken_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the darken blend mode.
- [func vImagePremultipliedAlphaBlendScreen_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendscreen_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the screen blend mode.
- [func vImagePremultipliedAlphaBlendMultiply_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendmultiply_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the multiply blend mode.
### Performing premultiplied alpha compositing with a permute
- [func vImagePremultipliedAlphaBlendWithPermute_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendwithpermute_argb8888(_:_:_:_:_:_:).md)
  Permutes the top 8-bit, 4-channel premultiplied buffer, and composites with the bottom buffer.
- [func vImagePremultipliedAlphaBlendWithPermute_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendwithpermute_rgba8888(_:_:_:_:_:_:).md)
  Permutes the top 8-bit, 4-channel premultiplied buffer, and composites with the bottom buffer.
### Performing premultiplied alpha compositing with a single alpha value
- [func vImagePremultipliedConstAlphaBlend_Planar8(UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedconstalphablend_planar8(_:_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit planar buffers and applies an extra alpha value to the top buffer.
- [func vImagePremultipliedConstAlphaBlend_PlanarF(UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedconstalphablend_planarf(_:_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit planar buffers and applies an extra alpha value to the top buffer.
- [func vImagePremultipliedConstAlphaBlend_ARGB8888(UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedconstalphablend_argb8888(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 8-bit-per-channel, 4-channel interleaved buffers and applies an extra alpha value to the top buffer.
- [func vImagePremultipliedConstAlphaBlend_ARGBFFFF(UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedconstalphablend_argbffff(_:_:_:_:_:).md)
  Performs premultiplied alpha compositing of two 32-bit-per-channel, 4-channel interleaved buffers and applies an extra alpha value to the top buffer.
### Performing nonpremultiplied to premultiplied alpha compositing
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_planar8(_:_:_:_:_:).md)
  Composites a nonpremultiplied 8-bit planar buffer over a premultiplied 8-bit planar buffer and generates a premultiplied result.
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_planarf(_:_:_:_:_:).md)
  Composites a nonpremultiplied 32-bit planar buffer over a premultiplied 32-bit planar buffer and generates a premultiplied result.
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_argb8888(_:_:_:_:).md)
  Composites a nonpremultiplied 8-bit-per-channel, ARGB buffer over a premultiplied ARGB buffer and generates a premultiplied result.
- [func vImageAlphaBlend_NonpremultipliedToPremultiplied_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagealphablend_nonpremultipliedtopremultiplied_argbffff(_:_:_:_:).md)
  Composites a nonpremultiplied 32-bit-per-channel, ARGB buffer over a premultiplied ARGB buffer and generates a premultiplied result.
### Converting from unpremultiplied to premultiplied format
- [func vImagePremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_planar8(_:_:_:_:).md)
  Transforms an 8-bit planar buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_planarf(_:_:_:_:).md)
  Transforms a 32-bit planar buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argb8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argb16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba16f(_:_:_:).md)
  Transforms a floating-point 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argb16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argbffff(_:_:_:).md)
  Transforms a floating-point 32-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgbaffff(_:_:_:).md)
  Transforms a floating-point 32-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
### Converting from premultiplied to unpremultiplied format
- [func vImageUnpremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_planar8(_:_:_:_:).md)
  Transforms an 8-bit planar buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_planarf(_:_:_:_:).md)
  Transforms a 32-bit planar buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argb8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argb16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba16f(_:_:_:).md)
  Transforms a floating-point 16-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argb16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgba16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_argbffff(_:_:_:).md)
  Transforms a 32-bit-per-channel, 4-channel ARGB buffer from premultiplied alpha format to nonpremultiplied alpha format.
- [func vImageUnpremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageunpremultiplydata_rgbaffff(_:_:_:).md)
  Transforms a 32-bit-per-channel, 4-channel RGBA buffer from premultiplied alpha format to nonpremultiplied alpha format.
### Clipping color values to alpha
- [func vImageClipToAlpha_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_planar8(_:_:_:_:).md)
  Clamps the values of an 8-bit planar buffer to the corresponding alpha values.
- [func vImageClipToAlpha_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_planarf(_:_:_:_:).md)
  Clamps the values of a 32-bit planar buffer to the corresponding alpha values.
- [func vImageClipToAlpha_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_argb8888(_:_:_:).md)
  Clamps the values of an 8-bit-per-channel, 4-channel ARGB buffer to the corresponding alpha values.
- [func vImageClipToAlpha_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_rgba8888(_:_:_:).md)
  Clamps the values of an 8-bit-per-channel, 4-channel RGBA buffer to the corresponding alpha values.
- [func vImageClipToAlpha_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_argbffff(_:_:_:).md)
  Clamps the values of a 32-bit-per-channel, 4-channel ARGB buffer to the corresponding alpha values.
- [func vImageClipToAlpha_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_rgbaffff(_:_:_:).md)
  Clamps the values of a 32-bit-per-channel, 4-channel RGBA buffer to the corresponding alpha values.

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/alpha-compositing)*