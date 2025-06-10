# vImageFlatten_ARGBFFFFToRGBFFF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Flattens a 32-bit-per-channel ARGB buffer against a solid background to produce a 32-bit-per-channel RGB result.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageFlatten_ARGBFFFFToRGBFFF(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>, _: UnsafePointer<Float>, _: Bool, _: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

##### Parameters

The function uses the following calculation to flatten the source image:

```c
 if( isImagePremultiplied )
     color = color + (1.0f - alpha) * backgroundColor
 else
     color = color * alpha + (1.0f - alpha) * backgroundColor
```

## See Also

- [func vImageFlatten_BGRAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_bgrafffftorgbfff(_:_:_:_:_:).md)
  Flattens a 32-bit-per-channel BGRA buffer against a solid background to produce a 32-bit-per-channel RGB result.
- [func vImageFlatten_RGBAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](vimageflatten_rgbafffftorgbfff(_:_:_:_:_:).md)
  Flattens a 32-bit-per-channel RGBA buffer against a solid background to produce a 32-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageflatten_argbfffftorgbfff(_:_:_:_:_:))*