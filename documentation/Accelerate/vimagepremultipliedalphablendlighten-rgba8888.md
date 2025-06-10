# vImagePremultipliedAlphaBlendLighten_RGBA8888(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the lighten blend mode.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vImagePremultipliedAlphaBlendLighten_RGBA8888(_ srcTop: UnsafePointer<vImage_Buffer>, _ srcBottom: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

## Mentions

- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

On return of this function, the value of each pixel in the destination buffer is:

```c
// For color channels:
uint8_t destColor = MAX( topColor +    ((255 - srcTopAlpha) *  srcBotomColor + 127) / 255,
                         bottomColor + ((255 - srcBottomAlpha) * srcTopColor + 127) / 255);
 
// For the alpha channel:
uint8_t alpha =  srcTopAlpha + ((255 - srcTopAlpha) * srcBottomAlpha + 127)/255;
```

## Parameters

- `srcTop`: The vImage buffer that provides the source top image.
- `srcBottom`: The vImage buffer that provides the source bottom image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImagePremultipliedAlphaBlendDarken_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablenddarken_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the darken blend mode.
- [func vImagePremultipliedAlphaBlendScreen_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendscreen_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the screen blend mode.
- [func vImagePremultipliedAlphaBlendMultiply_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendmultiply_rgba8888(_:_:_:_:).md)
  Performs alpha compositing of two 8-bit-per-channel, 4-channel BGRA buffers using the multiply blend mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablendlighten_rgba8888(_:_:_:_:))*