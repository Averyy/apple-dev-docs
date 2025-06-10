# Extracting channels

**Framework**: Accelerate

Extract one channel from a four-channel interleaved buffer.

## Topics

### Extracting channels
- [func vImageExtractChannel_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int, vImage_Flags) -> vImage_Error](vimageextractchannel_argb8888(_:_:_:_:).md)
  Extracts a single channel from an 8-bit-per-channel, 4-channel interleaved buffer and writes the result to an 8-bit planar buffer.
- [func vImageExtractChannel_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int, vImage_Flags) -> vImage_Error](vimageextractchannel_argb16u(_:_:_:_:).md)
  Extracts a single channel from an unsigned 16-bit-per-channel, 4-channel interleaved buffer and writes the result to an unsigned 16-bit planar buffer.
- [func vImageExtractChannel_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int, vImage_Flags) -> vImage_Error](vimageextractchannel_argbffff(_:_:_:_:).md)
  Extracts a single channel from a 32-bit-per-channel, 4-channel interleaved buffer and writes the result to a 32-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/extracting-channels)*