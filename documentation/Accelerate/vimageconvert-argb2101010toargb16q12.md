# vImageConvert_ARGB2101010ToARGB16Q12(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an ARGB2101010 32-bit, 4-channel interleaved buffer to a fixed-point 16-bit-per-channel, 4-channel interleaved buffer with permutation.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func vImageConvert_ARGB2101010ToARGB16Q12(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ RGB101010RangeMin: Int32, _ RGB101010RangeMax: Int32, _ permuteMap: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The `RGB101010RangeMin` and `RGB101010RangeMax` parameters allow you to specify that the function represents source pixel values that are outside of the range `0.0 ... 1.0`. For full-range pixel values, specify `RGB101010RangeMin` and `RGB101010RangeMax` as the following:

```swift
 RGB101010RangeMin = 0
 RGB101010RangeMax = 1023
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `RGB101010RangeMin`: The minimum pixel value for the source image range.
- `RGB101010RangeMax`: The maximum pixel value for the source image range.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGB2101010ToARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb2101010toargb16f(_:_:_:_:_:_:).md)
  Converts an ARGB2101010 32-bit, 4-channel interleaved buffer to a floating-point 16-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_XRGB2101010ToARGB16F(UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_xrgb2101010toargb16f(_:_:_:_:_:_:_:).md)
  Converts an XRGB2101010 32-bit, 4-channel interleaved buffer to a floating-point 16-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_XRGB2101010ToARGB16Q12(UnsafePointer<vImage_Buffer>, Pixel_16Q12, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_xrgb2101010toargb16q12(_:_:_:_:_:_:_:).md)
  Converts an XRGB2101010 32-bit, 4-channel interleaved buffer to a fixed-point 16-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_ARGB2101010ToARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb2101010toargbffff(_:_:_:_:_:_:).md)
  Converts an ARGB2101010 32-bit, 4-channel interleaved buffer to a floating-point 32-bit-per-channel, 4-channel interleaved buffer with permutation.
- [func vImageConvert_XRGB2101010ToARGBFFFF(UnsafePointer<vImage_Buffer>, Pixel_F, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_xrgb2101010toargbffff(_:_:_:_:_:_:_:).md)
  Converts an XRGB2101010 32-bit, 4-channel interleaved buffer to a floating-point 32-bit-per-channel, 4-channel interleaved buffer with permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb2101010toargb16q12(_:_:_:_:_:_:))*