# vImageConvert_ARGB16Q12To444CrYpCb10(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a fixed-point 16-bit-per-channel, 4-channel ARGB buffer to an 10-bit-per-channel 4:4:4 CrYpCb buffer.

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
func vImageConvert_ARGB16Q12To444CrYpCb10(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ info: UnsafePointer<vImage_ARGBToYpCbCr>, _ permuteMap: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `info`: A   structure that describes the conversion matrix, the range of the input and output pixels from the matrix, and clamping information.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGB8888To444CrYpCb8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444crypcb8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:4:4 CrYpCb buffer.
- [func vImageConvert_ARGB8888To444AYpCbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444aypcbcr8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:4:4 YpCbCr buffer.
- [func vImageConvert_ARGB8888To444CbYpCrA8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444cbypcra8(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 8-bit-per-channel 4:4:4 CrYpCbA buffer.
- [func vImageConvert_ARGB8888To444CrYpCb10(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444crypcb10(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 10-bit-per-channel 4:4:4 CrYpCb buffer.
- [func vImageConvert_ARGB8888To444AYpCbCr16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to444aypcbcr16(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to an 16-bit-per-channel 4:4:4 YpCbCr buffer.
- [func vImageConvert_ARGB16UTo444AYpCbCr16(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb16uto444aypcbcr16(_:_:_:_:_:).md)
  Converts an  unsigned 16-bit-per-channel, 4-channel ARGB buffer to an 16-bit-per-channel 4:4:4 AYpCbCr buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb16q12to444crypcb10(_:_:_:_:_:))*