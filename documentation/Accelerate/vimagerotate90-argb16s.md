# vImageRotate90_ARGB16S(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Rotates a signed 16-bit-per-channel, 4-channel interleaved image by a multiple of 90°.

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
func vImageRotate90_ARGB16S(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ rotationConstant: UInt8, _ backColor: UnsafePointer<Int16>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes from [`Error codes`](1578972-error-codes.md).

#### Discussion

This function maps the center point of the source image to the center point of the destination image. It doesn’t scale or resample; instead, the function copies unchanged individual pixels to new locations.

Depending on the relative sizes of the source image and the destination buffer, the function may clip parts of the source image. Areas outside the source image might appear in the destination image if you don’t pass a background color to the function.

The 90° and 270° rotations don’t rotate around the true center of the image if either of the following is true:

- The parities of the source height and the destination width don’t match. For example, the source height is odd and the destination width is even.
- The parities of the source width and the destination height don’t match. For example, the source width is odd and the destination height is even.

The 0° and 180° rotations don’t rotate around the true center of the image if either of the following is true:

- The parities of the source height and the destination height don’t match. For example, the source height is odd and the destination height is even.
- The parities of the source width and the destination width don’t match. For example, the source width is odd and the destination width is even.

To overcome this limitation, use the high-level rotation functions — for example, [`vImageRotate90_ARGB16U(_:_:_:_:_:)`](vimagerotate90_argb16u(_:_:_:_:_:).md).

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `rotationConstant`: A constant that specifies the rotation angle as a multiple of 90°. See   for the full list of supported rotation constants.
- `backColor`: A background color. If you set the   flag, pass a pixel value.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageRotate90_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_16U, vImage_Flags) -> vImage_Error](vimagerotate90_planar16u(_:_:_:_:_:).md)
  Rotates an unsigned 16-bit planar image by a multiple of 90°.
- [func vImageRotate90_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, Pixel_16F, vImage_Flags) -> vImage_Error](vimagerotate90_planar16f(_:_:_:_:_:).md)
  Rotates a floating-point 16-bit planar image by a multiple of 90°.
- [func vImageRotate90_CbCr16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate90_cbcr16f(_:_:_:_:_:).md)
  Rotates a floating-point 16-bit-per-channel, 2-channel interleaved image by a multiple of 90°.
- [func vImageRotate90_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagerotate90_argb16u(_:_:_:_:_:).md)
  Rotates an unsigned 16-bit-per-channel, 4-channel interleaved image by a multiple of 90°.
- [func vImageRotate90_ARGB16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, UnsafePointer<UInt16>!, vImage_Flags) -> vImage_Error](vimagerotate90_argb16f(_:_:_:_:_:).md)
  Rotates a floating-point 16-bit-per-channel, 4-channel interleaved image by a multiple of 90°.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagerotate90_argb16s(_:_:_:_:_:))*