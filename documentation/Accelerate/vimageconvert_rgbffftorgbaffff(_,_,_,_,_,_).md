# vImageConvert_RGBFFFtoRGBAFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce an RGBA result.

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
func vImageConvert_RGBFFFtoRGBAFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>!, _: Pixel_F, _: UnsafePointer<vImage_Buffer>, _: Bool, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

##### Parameters

- **rgbSrc**: The source vImage buffer that contains the red, green, and blue channels.
- **aSrc**: The source vImage buffer that contains the alpha channel. Set this value to `nil` to specify that the function sets the destination alpha as the constant destination alpha value.
- **alpha**: The constant destination alpha value. The function ignores this paramater if the `aSrc` parameter isn’t `nil`.
- **rgbaDest**: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](vimage_buffer/height.md), [`width`](vimage_buffer/width.md), and [`rowBytes`](vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- **premultiply**: A Boolean value that specifes whether the function premultiplies the color channels by the alpha channel.
- **flags**: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md).

If you specify `premultiply` as `true`, the function uses the following calculation to perform the conversion:

```objc
 r = (a * r)
 g = (a * g)
 b = (a * b)
```

## See Also

- [func vImageConvert_RGBFFFtoARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftoargbffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGBFFFtoBGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftobgraffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce a BGRA result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgbffftorgbaffff(_:_:_:_:_:_:))*