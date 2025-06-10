# vImageConvert_Planar8toARGB1555(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Interleaves four 8-bit planar buffers into an ARGB1555 4-channel interleaved buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_Planar8toARGB1555(_ srcA: UnsafePointer<vImage_Buffer>, _ srcR: UnsafePointer<vImage_Buffer>, _ srcG: UnsafePointer<vImage_Buffer>, _ srcB: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
    Pixel8 alpha =  1bitAlphaChannel * 255
    Pixel8 red   = (5bitRedChannel   * 255 + 15) / 31
    Pixel8 green = (5bitGreenChannel * 255 + 15) / 31
    Pixel8 blue  = (5bitBlueChannel  * 255 + 15) / 31
```

## Parameters

- `srcA`: The source vImage buffer that contains the alpha channel.
- `srcR`: The source vImage buffer that contains the red channel.
- `srcG`: The source vImage buffer that contains the green channel.
- `srcB`: The source vImage buffer that contains the blue channel.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_Planar8toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toargb8888(_:_:_:_:_:_:).md)
  Interleaves four 8-bit planar buffers into an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageConvert_Planar8ToARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>!, UnsafePointer<Float>!, vImage_Flags) -> vImage_Error](vimageconvert_planar8toargbffff(_:_:_:_:_:_:_:_:).md)
  Interleaves four 8-bit planar buffers into a floating-point 32-bit-per-channel, 4-channel interleaved ARGB buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8toargb1555(_:_:_:_:_:_:))*