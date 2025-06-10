# vImageFlatten_ARGBFFFF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs an alpha composite of a 32-bit-per-channel, 4-channel ARGB buffer over a solid background color.

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
func vImageFlatten_ARGBFFFF(_ argbSrc: UnsafePointer<vImage_Buffer>, _ argbDst: UnsafePointer<vImage_Buffer>, _ argbBackgroundColorPtr: UnsafePointer<Float>, _ isImagePremultiplied: Bool, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to flatten the source image:

```c
 resultAlpha = pixelAlpha + (1 - pixelAlpha) * backgroundAlpha
 
 if(isImagePremultiplied)
     resultColor = pixelColor + (1 - pixelAlpha) * backgroundColor
 else
     resultColor = pixelColor * pixelAlpha + (1 - pixelAlpha) * backgroundColor
```

## Parameters

- `argbSrc`: The source vImage buffer.
- `argbDst`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `argbBackgroundColorPtr`: A pixel value that defines the solid background color.
- `isImagePremultiplied`: A Boolean value that specifes whether the source image has premultiplied alpha.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageFlatten_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_rgbaffff(_:_:_:_:_:).md)
  Performs an alpha composite of a 32-bit-per-channel, 4-channel RGBA buffer over a solid background color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageflatten_argbffff(_:_:_:_:_:))*