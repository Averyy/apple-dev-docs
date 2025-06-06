# vImageCVImageFormat_GetAlphaHint(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the alpha hint of a Core Video image format.

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
func vImageCVImageFormat_GetAlphaHint(_ format: vImageConstCVImageFormat) -> Int32
```

#### Return Value

Zero if the alpha hint isn’t opaque, or if the hint isn’t set. Nonzero if the alpha hint is fully opaque, even if the encoded values for alpha in the image aren’t `1.0`.

#### Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md), return a [`vImageCVImageFormat`](vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetAlphaHint(_:)`](vimagecvimageformat_getalphahint(_:).md):

```swift
let alphaHint = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetAlphaHint(format)
}
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

- [var alphaIsOpaqueHint: Bool](vimagecvimageformat/alphaisopaquehint.md)
  The alpha hint of the Core Video image format.
- [func vImageCVImageFormat_SetAlphaHint(vImageCVImageFormat, Int32) -> vImage_Error](vimagecvimageformat_setalphahint(_:_:).md)
  Sets the alpha hint of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getalphahint(_:))*