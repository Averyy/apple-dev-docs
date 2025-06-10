# vImageConvert_Planar8toPlanar16F(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an 8-bit planar buffer to a floating-point 16-bit planar buffer.

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
func vImageConvert_Planar8toPlanar16F(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The conversion maps source pixels with a value of `0` to `0.0`, and maps source pixels with a value of `255` to `1.0`.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_8to16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_8to16q12(_:_:_:).md)
  Converts an 8-bit planar buffer to a fixed-point 16-bit planar buffer.
- [func vImageConvert_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Pixel_F, Pixel_F, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanarf(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a floating-point 32-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8toplanar16f(_:_:_:))*