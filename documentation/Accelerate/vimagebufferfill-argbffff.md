# vImageBufferFill_ARGBFFFF(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Fills a floating-point 32-bit-per-channel, 4-channel interleaved buffer with a specified color.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageBufferFill_ARGBFFFF(_ dest: UnsafePointer<vImage_Buffer>, _ color: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The following code fills the buffer with the specified color:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.InterleavedFx4>(
    size: .init(width: 1, height: 2))

let fillColor: [Pixel_F] = [64, 127, 192, 255]

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImageBufferFill_ARGBFFFF(buf,
                                 fillColor,
                                 vImage_Flags(kvImageNoFlags))
}

print(pixelBuffer.array)
// Prints:
//      "[64.0, 127.0, 192.0, 255.0,
//        64.0, 127.0, 192.0, 255.0]"
```

## Parameters

- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `color`: The fill color.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageBufferFill_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagebufferfill_cbcr8(_:_:_:).md)
  Fills an 8-bit-per-channel, 2-channel interleaved buffer with a specified color.
- [func vImageBufferFill_CbCr16U(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagebufferfill_cbcr16u(_:_:_:).md)
  Fills an unsigned 16-bit-per-channel, 2-channel interleaved buffer with a specified color.
- [func vImageBufferFill_CbCr16S(UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, vImage_Flags) -> vImage_Error](vimagebufferfill_cbcr16s(_:_:_:).md)
- [func vImageBufferFill_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagebufferfill_argb8888(_:_:_:).md)
  Fills an 8-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagebufferfill_argb16u(_:_:_:).md)
  Fills an unsigned 16-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, vImage_Flags) -> vImage_Error](vimagebufferfill_argb16s(_:_:_:).md)
  Fills a signed 16-bit-per-channel, 4-channel interleaved buffer with a specified color.
- [func vImageBufferFill_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagebufferfill_argb16f(_:_:_:).md)
  Fills a floating-point 16-bit-per-channel, 4-channel interleaved buffer with a specified color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebufferfill_argbffff(_:_:_:))*