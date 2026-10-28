# vImageCVImageFormat_GetAlphaHint(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
int vImageCVImageFormat_GetAlphaHint(vImageConstCVImageFormatRef format);
```

## Return Value

Zero if the alpha hint isn’t opaque, or if the hint isn’t set. Nonzero if the alpha hint is fully opaque, even if the encoded values for alpha in the image aren’t `1.0`.

## Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](./vimagecvimageformat_createwithcvpixelbuffer%28_%29.md), return a [`vImageCVImageFormat`](./vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](./vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](./vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetAlphaHint(_:)`](./vimagecvimageformat_getalphahint%28_%29.md):

**Swift**:

```swift
let alphaHint = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetAlphaHint(format)
}
```

**Objective-C**:

```objc
vImageConstCVImageFormatRef constFormat = cvImageFormat;

int alphaHint = vImageCVImageFormat_GetAlphaHint(constFormat);
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

### Related Documentation
- [var alphaIsOpaqueHint: Bool](./vimagecvimageformat/alphaisopaquehint.md)
  The alpha hint of the Core Video image format.
### Querying and setting the alpha hint
- [func vImageCVImageFormat_SetAlphaHint(vImageCVImageFormat, Int32) -> vImage_Error](./vimagecvimageformat_setalphahint%28_,_%29.md)
  Sets the alpha hint of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getalphahint(_:))*