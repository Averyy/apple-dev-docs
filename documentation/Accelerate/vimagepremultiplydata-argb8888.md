# vImagePremultiplyData_ARGB8888(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Transforms an 8-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImagePremultiplyData_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

## Mentions

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function multiplies color channels by the alpha channel using the following code:

```swift
uint8_t destColor = (src * alpha + 127) / 255;
uint8_t destAlpha = alpha;
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImagePremultiplyData_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_planar8(_:_:_:_:).md)
  Transforms an 8-bit planar buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_planarf(_:_:_:_:).md)
  Transforms a 32-bit planar buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba8888(_:_:_:).md)
  Transforms an 8-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argb16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba16u(_:_:_:).md)
  Transforms an unsigned 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba16f(_:_:_:).md)
  Transforms a floating-point 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argb16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgba16q12(_:_:_:).md)
  Transforms a fixed-point 16-bit-per-channel, 4-channel RGBA buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_argbffff(_:_:_:).md)
  Transforms a floating-point 32-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.
- [func vImagePremultiplyData_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagepremultiplydata_rgbaffff(_:_:_:).md)
  Transforms a floating-point 32-bit-per-channel, 4-channel ARGB buffer from nonpremultiplied alpha format to premultiplied alpha format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepremultiplydata_argb8888(_:_:_:))*