# vImageConvert_ARGB8888To420Yp8_Cb8_Cr8(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an 8-bit-per-channel, 4-channel ARGB buffer to planar Yp, Cb, and Cr buffers.

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
func vImageConvert_ARGB8888To420Yp8_Cb8_Cr8(_ src: UnsafePointer<vImage_Buffer>, _ destYp: UnsafePointer<vImage_Buffer>, _ destCb: UnsafePointer<vImage_Buffer>, _ destCr: UnsafePointer<vImage_Buffer>, _ info: UnsafePointer<vImage_ARGBToYpCbCr>, _ permuteMap: UnsafePointer<UInt8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

## Parameters

- `src`: The source vImage buffer.
- `destYp`: A pointer to the Yp destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the Yp destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destCb`: A pointer to the Cb destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the Cb destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destCr`: A pointer to the Cr destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the Cr destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `info`: A   structure that describes the conversion matrix, the range of the input and output pixels from the matrix, and clamping information.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGB8888To420Yp8_CbCr8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_ARGBToYpCbCr>, UnsafePointer<UInt8>!, vImage_Flags) -> vImage_Error](vimageconvert_argb8888to420yp8_cbcr8(_:_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel ARGB buffer to a planar Yp buffer and a 2-channel CbCr buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb8888to420yp8_cb8_cr8(_:_:_:_:_:_:_:))*