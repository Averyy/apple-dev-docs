# Functions that convert between integer planar buffers

**Framework**: Accelerate  
**Role**: API Collection

Convert the bit depths of planar integer image data.

## Topics

### Converting from 1-bit buffers
- [func vImageConvert_Planar1toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar1toplanar8%28_,_,_%29.md)
  Converts a 1-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_Indexed1toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](./vimageconvert_indexed1toplanar8%28_,_,_,_%29.md)
  Converts an indexed 1-bit planar buffer to an 8-bit planar buffer.
### Converting from 2-bit buffers
- [func vImageConvert_Planar2toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar2toplanar8%28_,_,_%29.md)
  Converts a 2-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_Indexed2toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](./vimageconvert_indexed2toplanar8%28_,_,_,_%29.md)
  Converts an indexed 2-bit planar buffer to an 8-bit planar buffer.
### Converting from 4-bit buffers
- [func vImageConvert_Planar4toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar4toplanar8%28_,_,_%29.md)
  Converts a 4-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_Indexed4toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](./vimageconvert_indexed4toplanar8%28_,_,_,_%29.md)
  Converts an indexed 4-bit planar buffer to an 8-bit planar buffer.
### Converting from 8-bit buffers
- [func vImageConvert_Planar8toPlanar1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toplanar1%28_,_,_,_,_%29.md)
  Converts an 8-bit planar buffer to a 1-bit planar buffer.
- [func vImageConvert_Planar8toPlanar2(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toplanar2%28_,_,_,_,_%29.md)
  Converts an 8-bit planar buffer to a 2-bit planar buffer.
- [func vImageConvert_Planar8toPlanar4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toplanar4%28_,_,_,_,_%29.md)
  Converts an 8-bit planar buffer to a 4-bit planar buffer.
- [func vImageConvert_Planar8toIndexed1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toindexed1%28_,_,_,_,_,_%29.md)
  Converts an 8-bit planar buffer to an indexed 1-bit planar buffer.
- [func vImageConvert_Planar8toIndexed2(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toindexed2%28_,_,_,_,_,_%29.md)
  Converts an 8-bit planar buffer to an indexed 2-bit planar buffer.
- [func vImageConvert_Planar8toIndexed4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar8toindexed4%28_,_,_,_,_,_%29.md)
  Converts an 8-bit planar buffer to an indexed 4-bit planar buffer.
- [func vImageConvert_Planar8To16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_planar8to16u%28_,_,_%29.md)
  Converts an 8-bit planar buffer to an unsigned 16-bit planar buffer.
### Converting from unsigned 12-bit-per-channel buffers
- [func vImageConvert_12UTo16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_12uto16u%28_,_,_%29.md)
  Converts an unsigned 12-bit planar buffer to an unsigned 16-bit planar buffer.
### Converting from unsigned 16-bit-per-channel buffers
- [func vImageConvert_16UToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_16utoplanar8%28_,_,_%29.md)
  Converts an unsigned 16-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_Planar16UtoPlanar8_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, vImage_Flags) -> vImage_Error](./vimageconvert_planar16utoplanar8_dithered%28_,_,_,_%29.md)
  Converts an unsigned 16-bit planar buffer to an 8-bit planar buffer using the specified dithering algorithm.
- [func vImageConvert_16UTo12U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageconvert_16uto12u%28_,_,_%29.md)
  Converts an unsigned 16-bit planar buffer to an unsigned 12-bit planar buffer.

## See Also

### Type conversion
- [Functions that convert between integer interleaved buffers](./functions-that-convert-between-integer-interleaved-buffers.md)
  Convert the bit depths of interleaved integer image data.
- [Functions that convert from integer planar buffers to noninteger planar buffers](./functions-that-convert-from-integer-planar-buffers-to-noninteger-planar-buffers.md)
  Convert planar integer image data to fixed- and floating-point format.
- [Functions that convert from integer interleaved buffers to noninteger interleaved buffers](./functions-that-convert-from-integer-interleaved-buffers-to-noninteger-interleaved-buffers.md)
  Convert interleaved integer image data to fixed- and floating-point format.
- [Functions that convert between noninteger planar buffers](./functions-that-convert-between-noninteger-planar-buffers.md)
  Convert the bit depths and formats of planar fixed- and floating-point image data.
- [Functions that convert between noninteger interleaved buffers](./functions-that-convert-between-noninteger-interleaved-buffers.md)
  Convert the bit depths and formats of interleaved fixed- and floating-point image data.
- [Functions that convert from noninteger planar buffers to integer planar buffers](./functions-that-convert-from-noninteger-planar-buffers-to-integer-planar-buffers.md)
  Convert planar fixed- and floating-point image data to integer format.
- [Functions that convert from noninteger interleaved buffers to integer interleaved buffers](./functions-that-convert-from-noninteger-interleaved-buffers-to-integer-interleaved-buffers.md)
  Convert interleaved fixed- and floating-point image data to integer format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/functions-that-convert-between-integer-planar-buffers)*