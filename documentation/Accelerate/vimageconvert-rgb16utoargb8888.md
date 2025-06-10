# vImageConvert_RGB16UToARGB8888(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an unsigned 16-bit-per-channel, 3-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer using permutation.

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
func vImageConvert_RGB16UToARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ permuteMap: UnsafePointer<UInt8>, _ copyMask: UInt8, _ backgroundColor: UnsafePointer<UInt8>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function doesn’t work in place.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `copyMask`: A bitmask that specifies the channel from the background color that the function copies to the destination channel at the corresponding index. The   bit corresponds to the alpha channel, the   bit corresponds to the red channel, the   corresponds to the green channel, and the   bit corresponds to the blue channel.
- `backgroundColor`: A 16-bit-per-channel, 4-channel pixel value that replaces the destination pixels based on the copy mask.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_RGB16UtoARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utoargb16u(_:_:_:_:_:_:).md)
  Combines an unsigned 16-bit-per-channel, 3-channel RGB buffer and either an unsigned 16-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGB16UtoBGRA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utobgra16u(_:_:_:_:_:_:).md)
  Combines an unsigned 16-bit-per-channel, 3-channel RGB buffer and either an unsigned 16-bit alpha buffer or constant alpha value to produce a BGRA result.
- [func vImageConvert_RGB16UtoRGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_16U, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb16utorgba16u(_:_:_:_:_:_:).md)
  Combines an unsigned 16-bit-per-channel, 3-channel RGB buffer and either an unsigned 16-bit alpha buffer or constant alpha value to produce an RGBA result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgb16utoargb8888(_:_:_:_:_:_:))*