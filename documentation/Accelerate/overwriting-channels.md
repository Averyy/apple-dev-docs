# Overwriting channels

**Framework**: Accelerate

Overwrite the channels of a buffer.

## Topics

### Overwriting with another buffer
- [func vImageSelectChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageselectchannels_argb8888(_:_:_:_:_:).md)
  Overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified channels of the corresponding pixels of a second buffer.
- [func vImageSelectChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageselectchannels_argbffff(_:_:_:_:_:).md)
  Overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer with the specified channels of the corresponding pixels of a second buffer.
- [func vImageOverwriteChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannels_argb8888(_:_:_:_:_:).md)
  Overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer with the corresponding pixels of a planar buffer.
- [func vImageOverwriteChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannels_argbffff(_:_:_:_:_:).md)
  Overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer with the corresponding pixels of a planar buffer.
### Overwriting with pixel values
- [func vImageOverwriteChannelsWithPixel_ARGB8888(UnsafePointer<UInt8>!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithpixel_argb8888(_:_:_:_:_:).md)
  Overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified channels of a pixel value.
- [func vImageOverwriteChannelsWithPixel_ARGB16U(UnsafePointer<UInt16>!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithpixel_argb16u(_:_:_:_:_:).md)
  Overwrites the channels of an unsigned 16-bit-per-channel, 4-channel interleaved buffer with the specified channels of a pixel value.
- [func vImageOverwriteChannelsWithPixel_ARGBFFFF(UnsafePointer<Float>!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithpixel_argbffff(_:_:_:_:_:).md)
  Overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer with the specified channels of a pixel value.
### Overwriting with scalar values
- [func vImageOverwriteChannelsWithScalar_Planar8(Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar8(_:_:_:).md)
  Overwrites an 8-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16U(Pixel_16U, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar16u(_:_:_:).md)
  Overwrites an unsigned 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16S(Pixel_16S, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar16s(_:_:_:).md)
  Overwrites a signed 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16F(Pixel_16F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar16f(_:_:_:).md)
  Overwrites a floating-point 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_PlanarF(Pixel_F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planarf(_:_:_:).md)
  Overwrites a floating-point 32-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_ARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_argb8888(_:_:_:_:_:).md)
  Overwrites the selected channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified scalar value.
- [func vImageOverwriteChannelsWithScalar_ARGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_argbffff(_:_:_:_:_:).md)
  Overwrites the selected channels of a 32-bit-per-channel, 4-channel interleaved buffer with the specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/overwriting-channels)*