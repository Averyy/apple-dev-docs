# vImageVerticalReflect_CbCr16F(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Reflects a floating-point 16-bit-per-channel, 2-channel interleaved image vertically across the center horizontal line.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func vImageVerticalReflect_CbCr16F(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageVerticalReflect_CbCr16F(const vImage_Buffer *src, const vImage_Buffer *dest, vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

This function doesn’t scale or resample; instead, it copies unchanged individual pixels to new locations. The source and destination buffers need to have the same height and the same width.

This function doesn’t work in place — that is, the source and destination buffers need to point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md), otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Related Documentation
- [Applying geometric transforms to images](./applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
### Applying vertical reflection to 16-bit-per-channel buffers
- [func vImageVerticalReflect_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageverticalreflect_planar16u%28_,_,_%29.md)
  Reflects an unsigned 16-bit planar image vertically across the center horizontal line.
- [func vImageVerticalReflect_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageverticalreflect_planar16f%28_,_,_%29.md)
  Reflects a floating-point 16-bit planar image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageverticalreflect_argb16u%28_,_,_%29.md)
  Reflects an unsigned 16-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageverticalreflect_argb16s%28_,_,_%29.md)
  Reflects a signed 16-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.
- [func vImageVerticalReflect_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageverticalreflect_argb16f%28_,_,_%29.md)
  Reflects a floating-point 16-bit-per-channel, 4-channel interleaved image vertically across the center horizontal line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageverticalreflect_cbcr16f(_:_:_:))*