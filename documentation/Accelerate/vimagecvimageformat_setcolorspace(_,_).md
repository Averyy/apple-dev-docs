# vImageCVImageFormat_SetColorSpace(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Sets the color space of a Core Video image format.

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
func vImageCVImageFormat_SetColorSpace(_ format: vImageCVImageFormat, _ colorspace: CGColorSpace!) -> vImage_Error
```

```c
vImage_Error vImageCVImageFormat_SetColorSpace(vImageCVImageFormatRef format, CGColorSpaceRef colorspace);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

For RGB, indexed, and grayscale images, the color space of a Core Video image format describes the image encoding.

For YpCbCr images, the color space describes the image encoding of the RGB image that’s the result of unapplying the RGB-to-YpCbCr conversion matrix.

## Parameters

- `format`: The Core Video image format to update.
- `colorspace`: The new color space for the format.

## See Also

### Related Documentation
- [var colorSpace: CGColorSpace?](./vimagecvimageformat/colorspace.md)
  The color space of the Core Video image format.
### Querying and setting the color space
- [func vImageCVImageFormat_GetColorSpace(vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>!](./vimagecvimageformat_getcolorspace%28_%29.md)
  Returns the color space of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_setcolorspace(_:_:))*