# Permuting Channels

**Framework**: Accelerate

Reorder the channels in an image.

## Topics

### Permuting channels
- [func vImagePermuteChannels_RGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimagepermutechannels_rgb888(_:_:_:_:).md)
  Permutes the channels of an 8-bit-per-channel, 3-channel interleaved buffer.
- [func vImagePermuteChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagepermutechannels_argb8888(_:_:_:_:).md)
  Permutes the channels of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImagePermuteChannels_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagepermutechannels_argb16u(_:_:_:_:).md)
  Permutes the channels of an unsigned 16-bit-per-channel, 4-channel interleaved buffer.
- [func vImagePermuteChannels_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagepermutechannels_argb16f(_:_:_:_:).md)
  Permutes the channels of a floating-point 16-bit-per-channel, 4-channel interleaved buffer.
- [func vImagePermuteChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagepermutechannels_argbffff(_:_:_:_:).md)
  Permutes the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer.
### Permuting channels with masked insert
- [func vImagePermuteChannelsWithMaskedInsert_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagepermutechannelswithmaskedinsert_argb8888(_:_:_:_:_:_:).md)
  Permutes and overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImagePermuteChannelsWithMaskedInsert_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagepermutechannelswithmaskedinsert_argb16u(_:_:_:_:_:_:).md)
  Permutes and overwrites the channels of an unsigned 16-bit-per-channel, 4-channel interleaved buffer.
- [func vImagePermuteChannelsWithMaskedInsert_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimagepermutechannelswithmaskedinsert_argbffff(_:_:_:_:_:_:).md)
  Permutes and overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/permuting-channels)*