# vImageConvert_RGBAFFFFtoRGBFFF(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Removes the alpha channel from a floating-point 32-bit-per-channel RGBA buffer to produce a floating-point 32-bit-per-channel RGB result.

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
func vImageConvert_RGBAFFFFtoRGBFFF(_ src: UnsafePointer<vImage_Buffer>!, _ dest: UnsafePointer<vImage_Buffer>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function copies the red, green, and blue source channels to the destination buffer.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_ARGBFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconvert_argbfffftorgbfff(_:_:_:).md)
  Removes the alpha channel from a floating-point 32-bit-per-channel ARGB buffer to produce a floating-point 32-bit-per-channel RGB result.
- [func vImageConvert_BGRAFFFFtoRGBFFF(UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconvert_bgrafffftorgbfff(_:_:_:).md)
  Removes the alpha channel from a floating-point 32-bit-per-channel BGRA buffer to produce a floating-point 32-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgbafffftorgbfff(_:_:_:))*