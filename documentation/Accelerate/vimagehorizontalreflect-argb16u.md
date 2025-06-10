# vImageHorizontalReflect_ARGB16U(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Reflects an unsigned 16-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.

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
func vImageHorizontalReflect_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function doesn’t scale or resample; instead, it copies unchanged individual pixels to new locations. The source and destination buffers must have the same height and the same width.

This function doesn’t work in place — that is, the source and destination buffers must point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  , otherwise, pass  .

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageHorizontalReflect_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_planar16u(_:_:_:).md)
  Reflects an unsigned 16-bit planar image horizontally across the center vertical line.
- [func vImageHorizontalReflect_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_planar16f(_:_:_:).md)
  Reflects a floating-point 16-bit planar image horizontally across the center vertical line.
- [func vImageHorizontalReflect_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_cbcr16f(_:_:_:).md)
  Reflects a floating-point 16-bit-per-channel, 2-channel interleaved image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGB16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argb16s(_:_:_:).md)
  Reflects a signed 16-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.
- [func vImageHorizontalReflect_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagehorizontalreflect_argb16f(_:_:_:).md)
  Reflects a floating-point 16-bit-per-channel, 4-channel interleaved image horizontally across the center vertical line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagehorizontalreflect_argb16u(_:_:_:))*