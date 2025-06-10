# vImageConvert_PlanarFToRGBX8888

**Framework**: Accelerate  
**Kind**: macro

Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
#define vImageConvert_PlanarFToRGBX8888(_red, _green, _blue, _alpha, _dest, _maxFloat, _minFloat, _flags)
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
uint8_t result = SATURATED_CLIP_0_to_255( 255.0f * ( srcPixel - minFloat ) / (maxFloat - minFloat) + 0.5f );
```

## Parameters

- `_red`: The source vImage buffer that contains the red channel.
- `_green`: The source vImage buffer that contains the green channel.
- `_blue`: The source vImage buffer that contains the blue channel.
- `_alpha`: The constant destination alpha value.
- `_dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_maxFloat`: A group of maximum pixel values, one per channel, in the same order as in the output pixels. The function clips larger values to these values in the destination image.
- `_minFloat`: A group of minimum pixel values, one per channel, in the same order as in the output pixels. The function clips smaller values to these values in the destination image.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_PlanarFToBGRX8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftobgrx8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved BGRX buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFToXRGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, UnsafePointer<Float>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgb8888(_:_:_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFtoRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftorgbfff(_:_:_:_:_:).md)
  Interleaves three floating-point 32-bit planar buffers into a floating-point 32-bit-per-channel, 3-channel interleaved buffer.
- [vImageConvert_PlanarFToRGBXFFFF](vimageconvert_planarftorgbxffff.md)
  Interleaves three 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved RGBX buffer with the specified constant alpha value.
- [func vImageConvert_PlanarFToXRGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planarftoxrgbffff(_:_:_:_:_:_:).md)
  Interleaves three 32-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved XRGB buffer with the specified constant alpha value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planarftorgbx8888)*