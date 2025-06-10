# vImageFlatten_ARGB16U(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs an alpha composite of an unsigned 16-bit-per-channel, 4-channel ARGB buffer over a solid background color.

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
func vImageFlatten_ARGB16U(_ argbSrc: UnsafePointer<vImage_Buffer>, _ argbDst: UnsafePointer<vImage_Buffer>, _ argbBackgroundColorPtr: UnsafePointer<UInt16>, _ isImagePremultiplied: Bool, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to flatten the source image:

```c
 pixelAlpha = CLAMP( 0, pixelAlpha, 4096);

 resultAlpha = (pixelAlpha * 4096 + (4096 - pixelAlpha) * backgroundAlpha + 2048) >> 12;
 
 if(isImagePremultiplied)
     resultColor = (pixelColor * 4096 + (4096 - pixelAlpha) * backgroundColor + 2048) >> 12
 else
     resultColor = (pixelColor * pixelAlpha + (4096 - pixelAlpha) * backgroundColor + 2048) >> 12
```

## Parameters

- `argbSrc`: The source vImage buffer.
- `argbDst`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `argbBackgroundColorPtr`: A pixel value that defines the solid background color.
- `isImagePremultiplied`: A Boolean value that specifes whether the source image has premultiplied alpha.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageFlatten_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_rgba16u(_:_:_:_:_:).md)
  Performs an alpha composite of an unsigned 16-bit-per-channel, 4-channel RGBA buffer over a solid background color.
- [func vImageFlatten_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_rgba16q12(_:_:_:_:_:).md)
  Performs an alpha composite of a fixed-point 16-bit-per-channel, 4-channel RGBA buffer over a solid background color.
- [func vImageFlatten_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_argb16q12(_:_:_:_:_:).md)
  Performs an alpha composite of a fixed-point 16-bit-per-channel, 4-channel ARGB buffer over a solid background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageflatten_argb16u(_:_:_:_:_:))*