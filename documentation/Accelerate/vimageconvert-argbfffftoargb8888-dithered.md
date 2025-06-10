# vImageConvert_ARGBFFFFtoARGB8888_dithered(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a floating-point 32-bit-per-channel, 4-channel buffer to an 8-bit-per-channel, 4-channel buffer using the specified dithering algorithm.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_ARGBFFFFtoARGB8888_dithered(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ maxFloat: UnsafePointer<Float>, _ minFloat: UnsafePointer<Float>, _ dither: Int32, _ permuteMap: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function supports the following dithering algorithms:

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image whose data you want to convert.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `maxFloat`: The four maximum source pixel values.
- `minFloat`: The four minimum source pixel values.
- `dither`: Type of dithering to apply to the image, if any.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_RGBFFFtoRGB888_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_F>, UnsafePointer<Pixel_F>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftorgb888_dithered(_:_:_:_:_:_:).md)
  Converts a floating-point 32-bit-per-channel, 3-channel buffer to an 8-bit-per-channel, 3-channel buffer using the specified dithering algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argbfffftoargb8888_dithered(_:_:_:_:_:_:_:))*