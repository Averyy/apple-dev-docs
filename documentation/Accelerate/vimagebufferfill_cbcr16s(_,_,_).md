# vImageBufferFill_CbCr16S(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func vImageBufferFill_CbCr16S(_ dest: UnsafePointer<vImage_Buffer>, _ color: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageBufferFill_CbCr16S(const vImage_Buffer *dest, const Pixel_16S16S color, vImage_Flags flags);
```

## Return Value

kvImageNoError                     Success

## Discussion

Fill the dest buffer with the pixel value.

## Parameters

- `dest`: A pointer to a valid and initialized vImage_Buffer struct, that points to a buffer containing destination pixels.
- `color`: A pixel value to fill the destination buffer.
- `flags`: \P kvImageNoFlags          Default operation \p kvImageDoNotTile        Disable internal multithreading.

## See Also

### Filling buffers
- [func vImageBufferFill_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](./vimagebufferfill_cbcr8%28_,_,_%29.md)
  Fills an 8-bit-per-channel, 2-channel interleaved buffer with a specified color.
- [func vImageBufferFill_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](./vimagebufferfill_cbcr16u%28_,_,_%29.md)
  Fills an unsigned 16-bit-per-channel, 2-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](./vimagebufferfill_argb8888%28_,_,_%29.md)
  Fills an 8-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](./vimagebufferfill_argb16u%28_,_,_%29.md)
  Fills an unsigned 16-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, vImage_Flags) -> vImage_Error](./vimagebufferfill_argb16s%28_,_,_%29.md)
  Fills a signed 16-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](./vimagebufferfill_argb16f%28_,_,_%29.md)
  Fills a floating-point 16-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](./vimagebufferfill_argbffff%28_,_,_%29.md)
  Fills a floating-point 32-bit-per-channel, 4-channel interleaved buffer with a specified color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebufferfill_cbcr16s(_:_:_:))*