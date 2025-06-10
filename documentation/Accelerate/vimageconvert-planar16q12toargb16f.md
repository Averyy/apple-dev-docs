# vImageConvert_Planar16Q12toARGB16F(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interleaves four fixed-point 16-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved buffer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func vImageConvert_Planar16Q12toARGB16F(_ alpha: UnsafePointer<vImage_Buffer>, _ red: UnsafePointer<vImage_Buffer>, _ green: UnsafePointer<vImage_Buffer>, _ blue: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The conversion maps source pixels with a value of `0` to `0.0`, and maps source pixels with a value of `4096` to `1.0`.

## Parameters

- `alpha`: The source vImage buffer that contains the alpha channel.
- `red`: The source vImage buffer that contains the red channel.
- `green`: The source vImage buffer that contains the green channel.
- `blue`: The source vImage buffer that contains the blue channel.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_Planar16Q12toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar16q12toargb8888(_:_:_:_:_:_:).md)
  Interleaves four fixed-point 16-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar16q12toargb16f(_:_:_:_:_:_:))*