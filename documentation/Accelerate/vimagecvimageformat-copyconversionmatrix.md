# vImageCVImageFormat_CopyConversionMatrix(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Copies an RGB-to-YpCbCr conversion matrix to an image format’s internal matrix.

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
func vImageCVImageFormat_CopyConversionMatrix(_ format: vImageCVImageFormat, _ matrix: UnsafeRawPointer, _ inType: vImageMatrixType) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

## Parameters

- `format`: The destination   instance.
- `matrix`: The matrix that the function copies to the destination image format.
- `inType`: The type of the matrix.

## See Also

- [func vImageCVImageFormat_GetConversionMatrix(vImageConstCVImageFormat, UnsafeMutablePointer<vImageMatrixType>!) -> UnsafeRawPointer!](vimagecvimageformat_getconversionmatrix(_:_:).md)
  Returns a pointer to the RGB-to-YpCbCr conversion matrix of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_copyconversionmatrix(_:_:_:))*