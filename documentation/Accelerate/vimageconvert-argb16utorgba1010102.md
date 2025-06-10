# vImageConvert_ARGB16UToRGBA1010102(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an RGBA1010102 32-bit, 4-channel buffer with permutation.

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
func vImageConvert_ARGB16UToRGBA1010102(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ RGB101010RangeMin: Int32, _ RGB101010RangeMax: Int32, _ permuteMap: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```c
 uint16_t *srcPixel = src.data;
 A16 = srcPixel[permuteMap[0]];
 R16 = srcPixel[permuteMap[1]];
 G16 = srcPixel[permuteMap[2]];
 B16 = srcPixel[permuteMap[3]];
 srcPixel += 4;
 
 int32_t R10, G10, B10;
 int32_t range10 = RGB101010RangeMax - RGB101010RangeMin;
 R10 = ((R16 * range10 + (USHRT_MAX >> 1)) / USHRT_MAX) + RGB101010RangeMin;
 G10 = ((G16 * range10 + (USHRT_MAX >> 1)) / USHRT_MAX) + RGB101010RangeMin;
 B10 = ((B16 * range10 + (USHRT_MAX >> 1)) / USHRT_MAX) + RGB101010RangeMin;
 A10 = ((A16 * 3 + (USHRT_MAX >> 1)) / USHRT_MAX);
 
 uint32_t *destPixel = dest.data;
 destPixel[0] = htonl((R10 << 22) | (G10 << 12) | (B10 << 2) | A10);
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

- [func vImageConvert_ARGB16UToARGB2101010(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoargb2101010(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an ARGB2101010 32-bit, 4-channel buffer with permutation.
- [func vImageConvert_ARGB16UToXRGB2101010(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, Int32, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16utoxrgb2101010(_:_:_:_:_:_:).md)
  Converts an unsigned 16-bit-per-channel, 4-channel interleaved buffer to an XRGB2101010 32-bit, 4-channel buffer with permutation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb16utorgba1010102(_:_:_:_:_:_:))*