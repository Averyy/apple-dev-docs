# vImageConvert_BGRA16UtoRGB16U(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Removes the alpha channel from an unsigned 16-bit-per-channel BGRA buffer to produce an unsigned 16-bit-per-channel RGB result.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_BGRA16UtoRGB16U(_ bgraSrc: UnsafePointer<vImage_Buffer>, _ rgbDest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function copies the red, green, and blue source channels to the destination buffer.

## Parameters

- `bgraSrc`: The source vImage buffer.
- `rgbDest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGB16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb16utorgb16u(_:_:_:).md)
  Removes the alpha channel from an unsigned 16-bit-per-channel ARGB buffer to produce an unsigned 16-bit-per-channel RGB result.
- [func vImageConvert_RGBA16UtoRGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba16utorgb16u(_:_:_:).md)
  Removes the alpha channel from an unsigned 16-bit-per-channel RGBA buffer to produce an unsigned 16-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_bgra16utorgb16u(_:_:_:))*