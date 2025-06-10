# vImageConvert_XRGB8888ToPlanar8(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into three 8-bit planar buffers and discards the first channel.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_XRGB8888ToPlanar8(_ src: UnsafePointer<vImage_Buffer>, _ red: UnsafePointer<vImage_Buffer>, _ green: UnsafePointer<vImage_Buffer>, _ blue: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The source and destination buffers must have the same height and width.

## Parameters

- `src`: The source vImage buffer.
- `red`: A pointer to the red destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the red destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `green`: A pointer to the green destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the green destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `blue`: A pointer to the blue destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the blue destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_BGRX8888ToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgrx8888toplanar8(_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into three 8-bit planar buffers and discards the last channel.
- [func vImageConvert_ARGB8888toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toplanar8(_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into four 8-bit planar buffers.
- [func vImageConvert_ARGB8888toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toplanar16q12(_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into four fixed-point 16-bit planar buffers.
- [func vImageConvert_ARGB8888toPlanarF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toplanarf(_:_:_:_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 4-channel interleaved buffer into four floating-point 32-bit planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_xrgb8888toplanar8(_:_:_:_:_:))*