# vImageConvert_Indexed2toPlanar8(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an indexed 2-bit planar buffer to an 8-bit planar buffer.

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
func vImageConvert_Indexed2toPlanar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ colors: UnsafePointer<Pixel_8>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

For each destination pixel, the conversion uses the lookup table value with the corresponding source pixel value as the index.

## Parameters

- `src`: The source vImage buffer. Because the source pixel format is smaller than a byte, there are multiple pixels in each byte of the data buffer. This function interprets pixels as big-endian order. That is, the low-indexed pixel is in the high-order bits of the byte. For example, the eight 1-bit pixels `0b11100011` map to the eight 8-bit pixels `[255, 255, 255, 0, 0, 0, 255, 255]`. The conversion ignores any unused bits of the final byte of a row when a scanline ends in the middle of a byte.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](vimage_buffer/height.md), [`width`](vimage_buffer/width.md), and [`rowBytes`](vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `colors`: The lookup table.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

## See Also

- [func vImageConvert_Planar2toPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar2toplanar8(_:_:_:).md)
  Converts a 2-bit planar buffer to an 8-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_indexed2toplanar8(_:_:_:_:))*