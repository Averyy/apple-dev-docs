# vImageConvert_422CrYpCbYpCbYpCbYpCrYpCrYp10ToARGB16Q12(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a 10-bit-per-channel 4:2:2 CrYpCbYpCbYpCbYpCrYpCrYp buffer to a fixed-point 16-bit-per-channel, 4-channel ARGB buffer.

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
func vImageConvert_422CrYpCbYpCbYpCbYpCrYpCrYp10ToARGB16Q12(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ info: UnsafePointer<vImage_YpCbCrToARGB>, _ permuteMap: UnsafePointer<UInt8>!, _ alpha: Pixel_16Q12, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `info`: A   structure that describes the conversion matrix, the range of the input and output pixels from the matrix, and clamping information.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `alpha`: The constant destination alpha value.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_422YpCbYpCr8ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_YpCbCrToARGB>, UnsafePointer<UInt8>!, UInt8, vImage_Flags) -> vImage_Error](vimageconvert_422ypcbypcr8toargb8888(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel 4:2:2 YpCbYpCr buffer to an 8-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_422CbYpCrYp8ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_YpCbCrToARGB>, UnsafePointer<UInt8>!, UInt8, vImage_Flags) -> vImage_Error](vimageconvert_422cbypcryp8toargb8888(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel 4:2:2 CbYpCrYp buffer to an 8-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_422CbYpCrYp16ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_YpCbCrToARGB>, UnsafePointer<UInt8>!, UInt8, vImage_Flags) -> vImage_Error](vimageconvert_422cbypcryp16toargb8888(_:_:_:_:_:_:).md)
  Converts a 16-bit-per-channel 4:2:2 CbYpCrYp buffer to an 8-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_422CbYpCrYp8_AA8ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_YpCbCrToARGB>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_422cbypcryp8_aa8toargb8888(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel 4:2:2 CbYpCrYp buffer and an 8-bit alpha buffer to an 8-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_422CbYpCrYp16ToARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_YpCbCrToARGB>, UnsafePointer<UInt8>!, UInt16, vImage_Flags) -> vImage_Error](vimageconvert_422cbypcryp16toargb16u(_:_:_:_:_:_:).md)
  Converts a 16-bit-per-channel 4:2:2 CbYpCrYp buffer to an unsigned 16-bit-per-channel, 4-channel ARGB buffer.
- [func vImageConvert_422CrYpCbYpCbYpCbYpCrYpCrYp10ToARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_YpCbCrToARGB>, UnsafePointer<UInt8>!, UInt8, vImage_Flags) -> vImage_Error](vimageconvert_422crypcbypcbypcbypcrypcryp10toargb8888(_:_:_:_:_:_:).md)
  Converts a 10-bit-per-channel 4:2:2 CrYpCbYpCbYpCbYpCrYpCrYp buffer to a 8-bit-per-channel, 4-channel ARGB buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_422crypcbypcbypcbypcrypcryp10toargb16q12(_:_:_:_:_:_:))*