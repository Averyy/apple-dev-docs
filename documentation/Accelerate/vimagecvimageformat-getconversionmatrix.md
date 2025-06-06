# vImageCVImageFormat_GetConversionMatrix(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a pointer to the RGB-to-YpCbCr conversion matrix of a Core Video image format.

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
func vImageCVImageFormat_GetConversionMatrix(_ format: vImageConstCVImageFormat, _ outType: UnsafeMutablePointer<vImageMatrixType>!) -> UnsafeRawPointer!
```

#### Return Value

A pointer to the conversion matrix.

#### Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md), return a [`vImageCVImageFormat`](vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetConversionMatrix(_:_:)`](vimagecvimageformat_getconversionmatrix(_:_:).md):

```swift
let conversionMatrixPointer = withUnsafeBytes(of: cvImageFormat) { bytes in
    var outType = UInt32()
    
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetConversionMatrix(format, &outType)
}
```

## Parameters

- `format`: The Core Video image format to query.
- `outType`: A pointer to a  .

## See Also

- [func vImageCVImageFormat_CopyConversionMatrix(vImageCVImageFormat, UnsafeRawPointer, vImageMatrixType) -> vImage_Error](vimagecvimageformat_copyconversionmatrix(_:_:_:).md)
  Copies an RGB-to-YpCbCr conversion matrix to an image format’s internal matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getconversionmatrix(_:_:))*