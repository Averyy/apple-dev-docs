# vImageFlatten_BGRA8888ToBGR888

**Framework**: Accelerate  
**Kind**: macro

Flattens an 8-bit-per-channel BGRA buffer against a solid background to produce an 8-bit-per-channel BGR result.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
#define vImageFlatten_BGRA8888ToBGR888(_bgra8888Src, _bgr888Dest, _backgroundColor, _isImagePremultiplied, _flags)
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to flatten the source image:

```c
 if( isImagePremultiplied )
     color = (color * 255 + (255 - alpha) * backgroundColor + 127) / 255
 else
     color = (color * alpha + (255 - alpha) * backgroundColor + 127) / 255
```

## Parameters

- `_bgra8888Src`: The source vImage buffer.
- `_bgr888Dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `_backgroundColor`: A pixel value that defines the solid background color.
- `_isImagePremultiplied`: A Boolean value that specifes whether the source image has premultiplied alpha.
- `_flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageFlatten_ARGB8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_argb8888torgb888(_:_:_:_:_:).md)
  Flattens an 8-bit-per-channel ARGB buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [func vImageFlatten_BGRA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_bgra8888torgb888(_:_:_:_:_:).md)
  Flattens an 8-bit-per-channel BGRA buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [func vImageFlatten_RGBA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_rgba8888torgb888(_:_:_:_:_:).md)
  Flattens an 8-bit-per-channel RGBA buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [vImageFlatten_RGBA8888ToBGR888](vimageflatten_rgba8888tobgr888.md)
  Flattens an 8-bit-per-channel RGBA buffer against a solid background to produce an 8-bit-per-channel BGR result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageflatten_bgra8888tobgr888)*