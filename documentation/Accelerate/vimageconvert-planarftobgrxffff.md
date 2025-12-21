# vImageConvert_PlanarFToBGRXFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interleaves four floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel BGRXARGB interleaved buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_PlanarFToBGRXFFFF(_ blue: UnsafePointer<vImage_Buffer>, _ green: UnsafePointer<vImage_Buffer>, _ red: UnsafePointer<vImage_Buffer>, _ alpha: Pixel_F, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The source and destination buffers need to have the same height and width.

## Parameters

- `blue`: The source vImage buffer that contains the blue channel.
- `green`: The source vImage buffer that contains the green channel.
- `red`: The source vImage buffer that contains the red channel.
- `alpha`: The source vImage buffer that contains the alpha channel.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_PlanarFToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoargb8888(_:_:_:_:_:_:_:_:).md)
  Interleaves four 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_PlanarFtoARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoargbffff(_:_:_:_:_:_:).md)
  Interleaves four floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel ARGB interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftobgrxffff(_:_:_:_:_:_:))*