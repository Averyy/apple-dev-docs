# vImageConvert_Planar1toPlanar8(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a 1-bit planar buffer to an 8-bit planar buffer.

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
func vImageConvert_Planar1toPlanar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The conversion uses the source pixel value multiplied by `255` as the corresponding destination pixel value.

## Parameters

- `src`: The conversion ignores any unused bits of the final byte of a row when a scanline ends in the middle of a byte.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_Indexed1toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](vimageconvert_indexed1toplanar8(_:_:_:_:).md)
  Converts an indexed 1-bit planar buffer to an 8-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar1toplanar8(_:_:_:))*