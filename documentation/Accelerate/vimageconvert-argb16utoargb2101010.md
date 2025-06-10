# vImageConvert_ARGB16UToARGB2101010(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an ARGB2101010 32-bit, 4-channel buffer with permutation.

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
func vImageConvert_ARGB16UToARGB2101010(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ RGB101010RangeMin: Int32, _ RGB101010RangeMax: Int32, _ permuteMap: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```c
 uint8_t *srcPixel = src.data;
 R8 = srcPixel[permuteMap[1]];
 G8 = srcPixel[permuteMap[2]];
 B8 = srcPixel[permuteMap[3]];
 srcPixel += 4;
 
 int32_t R10, G10, B10;
 int32_t range10 = RGB101010RangeMax - RGB101010RangeMin;
 int32_t rounding = UCHAR_MAX >> 1;
 R10 = ((R8 * range10 + rounding) / UCHAR_MAX) + RGB101010RangeMin;
 G10 = ((G8 * range10 + rounding) / UCHAR_MAX) + RGB101010RangeMin;
 B10 = ((B8 * range10 + rounding) / UCHAR_MAX) + RGB101010RangeMin;
 
 uint32_t *destPixel = dest.data;
 destPixel[0] = (R10 << 20) | (G10 << 10) | (B10 << 0);
 destPixel += 1;

```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `RGB101010RangeMin`: The minimum pixel value for the destination image.
- `RGB101010RangeMax`: The maximum pixel value for the destination image.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGB16UToRGBA1010102(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16utorgba1010102(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an RGBA1010102 32-bit, 4-channel buffer with permutation.
- [func vImageConvert_ARGB16UToXRGB2101010(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoxrgb2101010(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an XRGB2101010 32-bit, 4-channel buffer with permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb16utoargb2101010(_:_:_:_:_:_:))*