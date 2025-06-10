# vImageConvert_PlanarFToBGRX8888(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.

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
func vImageConvert_PlanarFToBGRX8888(_ blue: UnsafePointer<vImage_Buffer>, _ green: UnsafePointer<vImage_Buffer>, _ red: UnsafePointer<vImage_Buffer>, _ alpha: Pixel_8, _ dest: UnsafePointer<vImage_Buffer>, _ maxFloat: UnsafePointer<Float>, _ minFloat: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
uint8_t result = SATURATED_CLIP_0_to_255( 255.0f * ( srcPixel - minFloat ) / (maxFloat - minFloat) + 0.5f );
```

## Parameters

- `blue`: The source vImage buffer that contains the blue channel.
- `green`: The source vImage buffer that contains the green channel.
- `red`: The source vImage buffer that contains the red channel.
- `alpha`: The constant destination alpha value.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `maxFloat`: The maximum pixel value for the destination image.
- `minFloat`: The minimum pixel value for the destination image.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_PlanarFToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgb8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftorgbfff(_:_:_:_:_:).md)
  Interleaves three floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 3-channel interleaved buffer.
- [func vImageConvert_PlanarFToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgbffff(_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftobgrx8888(_:_:_:_:_:_:_:_:))*