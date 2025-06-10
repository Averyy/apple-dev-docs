# vImageConvert_ARGBFFFFtoPlanarF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into four floating-point 38-bit planar buffers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_ARGBFFFFtoPlanarF(_ srcARGB: UnsafePointer<vImage_Buffer>, _ destA: UnsafePointer<vImage_Buffer>, _ destR: UnsafePointer<vImage_Buffer>, _ destG: UnsafePointer<vImage_Buffer>, _ destB: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The source and destination buffers must have the same height and width.

## Parameters

- `srcARGB`: The source vImage buffer.
- `destA`: A pointer to the alpha destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the alpha destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destR`: A pointer to the red destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the red destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destG`: A pointer to the green destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the green destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destB`: A pointer to the blue destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the blue destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGBFFFFtoPlanar8(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_argbfffftoplanar8(_:_:_:_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into four 8-bit planar buffers.
- [func vImageConvert_BGRXFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_bgrxfffftoplanarf(_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into three floating-point 32-bit planar buffers and discards the last channel.
- [func vImageConvert_XRGBFFFFToPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_xrgbfffftoplanarf(_:_:_:_:_:).md)
  Deinterleaves a floating-point 32-bit-per-channel, 4-channel interleaved buffer into three floating-point 32-bit planar buffers and discards the first channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argbfffftoplanarf(_:_:_:_:_:_:))*