# Applying a flood fill to an image

**Framework**: Accelerate  
**Role**: API Collection

Fill connected components of an image with a new color.

## Topics

### Flood-filling buffers
- [Applying flood fills to an image](./applying-flood-fills-to-an-image.md)
  Fill consistently colored connected parts of an image with a new color.
- [func vImageFloodFill_Planar8(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, Pixel_8, Int32, vImage_Flags) -> vImage_Error](./vimagefloodfill_planar8%28_,_,_,_,_,_,_%29.md)
  Applies a flood-fill operation to an 8-bit planar image.
- [func vImageFloodFill_Planar16U(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, Pixel_16U, Int32, vImage_Flags) -> vImage_Error](./vimagefloodfill_planar16u%28_,_,_,_,_,_,_%29.md)
  Applies a flood fill-operation to an unsigned 16-bit planar image.
- [func vImageFloodFill_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UInt8>!, Int32, vImage_Flags) -> vImage_Error](./vimagefloodfill_argb8888%28_,_,_,_,_,_,_%29.md)
  Applies a flood-fill operation to an 8-bit-per-channel, four-channel interleaved image.
- [func vImageFloodFill_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UInt16>!, Int32, vImage_Flags) -> vImage_Error](./vimagefloodfill_argb16u%28_,_,_,_,_,_,_%29.md)
  Applies a flood-fill operation to an unsigned 16-bit-per-channel, four-channel interleaved image.

## See Also

### Applying color transforms to images
- [Transforming with lookup tables](./transforming-with-lookup-tables.md)
  Use lookup tables to apply color transformations to images.
- [Transforming with polynomials](./transforming-with-polynomials.md)
  Use polynomials to apply color transformations to images.
- [Transforming with matrix multiplication](./transforming-with-matrix-multiplication.md)
  Use matrix multiplication to apply color transformations to images.
- [Transforming with a gamma function](./transforming-with-a-gamma-function.md)
  Use gamma functions to apply color transformations to images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-a-flood-fill-to-an-image)*