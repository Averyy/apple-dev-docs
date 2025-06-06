# vImageCVImageFormat_GetColorSpace(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the color space of a Core Video image format.

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
func vImageCVImageFormat_GetColorSpace(_ format: vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>!
```

#### Return Value

The color space of the specified image format.

#### Discussion

For RGB, indexed, and grayscale images, the color space of a Core Video image format describes the image encoding.

For YpCbCr images, the color space describes the image encoding of the RGB image that’s the result of unapplying the RGB-to-YpCbCr conversion matrix.

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md), return a [`vImageCVImageFormat`](vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetColorSpace(_:)`](vimagecvimageformat_getcolorspace(_:).md):

```swift
let colorSpace = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetColorSpace(format)
}
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

- [var colorSpace: CGColorSpace?](vimagecvimageformat/colorspace.md)
  The color space of the Core Video image format.
- [func vImageCVImageFormat_SetColorSpace(vImageCVImageFormat, CGColorSpace!) -> vImage_Error](vimagecvimageformat_setcolorspace(_:_:).md)
  Sets the color space of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getcolorspace(_:))*