# vImageCVImageFormat_GetFormatCode(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the four-character code that encodes the pixel format of a Core Video image format.

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
func vImageCVImageFormat_GetFormatCode(_ format: vImageConstCVImageFormat) -> UInt32
```

#### Return Value

The four-character code of the image format, such as [`kCVPixelFormatType_420YpCbCr8Planar`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8Planar).

#### Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md), return a [`vImageCVImageFormat`](vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetFormatCode(_:)`](vimagecvimageformat_getformatcode(_:).md):

```swift
let formatCode = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetFormatCode(format)
}
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

- [var formatCode: UInt32](vimagecvimageformat/formatcode.md)
  The four-character code that encodes the pixel format of the Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getformatcode(_:))*