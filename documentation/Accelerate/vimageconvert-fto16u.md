# vImageConvert_FTo16U(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a floating-point 32-bit planar buffer to an unsigned 16-bit planar buffer.

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
func vImageConvert_FTo16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ offset: Float, _ scale: Float, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
uint16_t result = SATURATED_CLIP_0_to_USHRT_MAX( (srcPixel - offset) / scale  + 0.5f);
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `offset`: The offset value that the conversion subtracts from each pixel.
- `scale`: The scale value that the conversion divides each pixel by.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageconvert_planarftoplanar8(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_PlanarFtoPlanar8_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planarftoplanar8_dithered(_:_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to an 8-bit planar buffer using the specified dithering algorithm.
- [func vImageConvert_FTo16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Float, Float, vImage_Flags) -> vImage_Error](vimageconvert_fto16s(_:_:_:_:_:).md)
  Converts a floating-point 32-bit planar buffer to a signed 16-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_fto16u(_:_:_:_:_:))*