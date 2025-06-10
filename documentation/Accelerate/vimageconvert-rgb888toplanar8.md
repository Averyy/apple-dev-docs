# vImageConvert_RGB888toPlanar8(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Deinterleaves an 8-bit-per-channel, 3-channel interleaved buffer into three 8-bit planar buffers.

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
func vImageConvert_RGB888toPlanar8(_ rgbSrc: UnsafePointer<vImage_Buffer>, _ redDest: UnsafePointer<vImage_Buffer>, _ greenDest: UnsafePointer<vImage_Buffer>, _ blueDest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The source and destination buffers must have the same height and width.

## Parameters

- `rgbSrc`: The source vImage buffer.
- `redDest`: A pointer to the red destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the red destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `greenDest`: A pointer to the green destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the green destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `blueDest`: A pointer to the blue destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the blue destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_RGB888toPlanar16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgb888toplanar16q12(_:_:_:_:_:).md)
  Deinterleaves an 8-bit-per-channel, 3-channel interleaved buffer into three fixed-point 16-bit planar buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgb888toplanar8(_:_:_:_:_:))*