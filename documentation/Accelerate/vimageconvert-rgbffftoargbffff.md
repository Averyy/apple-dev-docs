# vImageConvert_RGBFFFtoARGBFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce an ARGB result.

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
func vImageConvert_RGBFFFtoARGBFFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>!, _: Pixel_F, _: UnsafePointer<vImage_Buffer>, _: Bool, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

##### Parameters

If you specify `premultiply` as `true`, the function uses the following calculation to perform the conversion:

```objc
 r = (a * r)
 g = (a * g)
 b = (a * b)
```

## See Also

- [func vImageConvert_RGBFFFtoBGRAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftobgraffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce a BGRA result.
- [func vImageConvert_RGBFFFtoRGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_F, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgbffftorgbaffff(_:_:_:_:_:_:).md)
  Combines a floating-point 32-bit-per-channel, 3-channel RGB buffer and either an 32-bit alpha buffer or constant alpha value to produce an RGBA result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgbffftoargbffff(_:_:_:_:_:_:))*