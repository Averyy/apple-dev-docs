# vImageCVImageFormat_SetAlphaHint(_:_:)

**Framework**: Accelerate  
**Kind**: func

Sets the alpha hint of a Core Video image format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCVImageFormat_SetAlphaHint(_ format: vImageCVImageFormat, _ alphaIsOne: Int32) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

When an image format contains an alpha channel, but the image is fully opaque, set this property to a nonzero value.

## Parameters

- `format`: The Core Video image format to update.
- `alphaIsOne`: The new value of the alpha hint.

## See Also

- [var alphaIsOpaqueHint: Bool](vimagecvimageformat/alphaisopaquehint.md)
  The alpha hint of the Core Video image format.
- [func vImageCVImageFormat_GetAlphaHint(vImageConstCVImageFormat) -> Int32](vimagecvimageformat_getalphahint(_:).md)
  Returns the alpha hint of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_setalphahint(_:_:))*