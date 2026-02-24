# vImageConvert_Planar4toPlanar8(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts a 4-bit planar buffer to an 8-bit planar buffer.

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
func vImageConvert_Planar4toPlanar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The conversion uses the source pixel value multiplied by `17` as the corresponding destination pixel value.

## Parameters

- `src`: The source vImage buffer. Because the source pixel format is smaller than a byte, there are multiple pixels in each byte of the data buffer. This function interprets pixels as big-endian order. That is, the low-indexed pixel is in the high-order bits of the byte. For example, the eight 1-bit pixels `0b11100011` map to the eight 8-bit pixels `[255, 255, 255, 0, 0, 0, 255, 255]`. The conversion ignores any unused bits of the final byte of a row when a scanline ends in the middle of a byte.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](vimage_buffer/height.md), [`width`](vimage_buffer/width.md), and [`rowBytes`](vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

## See Also

- [func vImageConvert_Indexed4toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Pixel_8>, vImage_Flags) -> vImage_Error](vimageconvert_indexed4toplanar8(_:_:_:_:).md)
  Converts an indexed 4-bit planar buffer to an 8-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar4toplanar8(_:_:_:))*