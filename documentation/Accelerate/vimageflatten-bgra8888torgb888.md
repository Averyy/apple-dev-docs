# vImageFlatten_BGRA8888ToRGB888(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Flattens an 8-bit-per-channel BGRA buffer against a solid background to produce an 8-bit-per-channel RGB result.

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
func vImageFlatten_BGRA8888ToRGB888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<UInt8>, _: Bool, _: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

##### Parameters

- **bgra8888Src**: The source vImage buffer.
- **rgb888dest**: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](vimage_buffer/height.md), [`width`](vimage_buffer/width.md), and [`rowBytes`](vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- **backgroundColor**: A pixel value that defines the solid background color.
- **isImagePremultiplied**: A Boolean value that specifes whether the source image has premultiplied alpha.
- **flags**: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

The function uses the following calculation to flatten the source image:

```c
 if( isImagePremultiplied )
     color = (color * 255 + (255 - alpha) * backgroundColor + 127) / 255
 else
     color = (color * alpha + (255 - alpha) * backgroundColor + 127) / 255
```

## See Also

- [func vImageFlatten_ARGB8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_argb8888torgb888(_:_:_:_:_:).md)
  Flattens an 8-bit-per-channel ARGB buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [func vImageFlatten_RGBA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_rgba8888torgb888(_:_:_:_:_:).md)
  Flattens an 8-bit-per-channel RGBA buffer against a solid background to produce an 8-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageflatten_bgra8888torgb888(_:_:_:_:_:))*