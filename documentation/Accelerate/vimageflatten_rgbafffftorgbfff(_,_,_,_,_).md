# vImageFlatten_RGBAFFFFToRGBFFF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Flattens a 32-bit-per-channel RGBA buffer against a solid background to produce a 32-bit-per-channel RGB result.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 6.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageFlatten_RGBAFFFFToRGBFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<Float>, _: Bool, _: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageFlatten_RGBAFFFFToRGBFFF(const vImage_Buffer *, const vImage_Buffer *, const Pixel_FFFF , bool , vImage_Flags );
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

##### Parameters

- **rgbaFFFFSrc**: The source vImage buffer.
- **rgbFFFdest**: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- **backgroundColor**: A floating-point interleaved pixel value.
- **isImagePremultiplied**: A Boolean value that specifes whether the source image has premultiplied alpha.
- **flags**: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

The function uses the following calculation to flatten the source image:

```c
 if( isImagePremultiplied )
     color = color + (1.0f - alpha) * backgroundColor
 else
     color = color * alpha + (1.0f - alpha) * backgroundColor
```

## See Also

### Flattening 4-channel, 32-bit images to three channels
- [func vImageFlatten_ARGBFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argbfffftorgbfff%28_,_,_,_,_%29.md)
  Flattens a 32-bit-per-channel ARGB buffer against a solid background to produce a 32-bit-per-channel RGB result.
- [func vImageFlatten_BGRAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_bgrafffftorgbfff%28_,_,_,_,_%29.md)
  Flattens a 32-bit-per-channel BGRA buffer against a solid background to produce a 32-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageflatten_rgbafffftorgbfff(_:_:_:_:_:))*