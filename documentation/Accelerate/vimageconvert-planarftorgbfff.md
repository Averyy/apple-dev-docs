# vImageConvert_PlanarFtoRGBFFF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interleaves three floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 3-channel interleaved buffer.

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
func vImageConvert_PlanarFtoRGBFFF(_ planarRed: UnsafePointer<vImage_Buffer>, _ planarGreen: UnsafePointer<vImage_Buffer>, _ planarBlue: UnsafePointer<vImage_Buffer>, _ rgbDest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The source and destination buffers must have the same height and width.

## Parameters

- `planarRed`: The source vImage buffer that contains the red channel.
- `planarGreen`: The source vImage buffer that contains the green channel.
- `planarBlue`: The source vImage buffer that contains the blue channel.
- `rgbDest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_PlanarFToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftobgrx8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgb8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgbffff(_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftorgbfff(_:_:_:_:_:))*