# vImageConstCVImageFormat

**Framework**: Accelerate  
**Kind**: class

An immutable description of image encoding in a Core Video pixel buffer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class vImageConstCVImageFormat
```

#### Discussion

Use [`vImageCVImageFormat_Copy(_:)`](vimagecvimageformat_copy(_:).md) to create a mutable copy of a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) instance.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class vImageCVImageFormat](vimagecvimageformat.md)
  A mutable description of image encoding in a Core Video pixel buffer.
- [func vImageCVImageFormat_CreateWithCVPixelBuffer(CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_createwithcvpixelbuffer(_:).md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [func vImageCVImageFormat_Create(UInt32, UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, CFString!, CGColorSpace!, Int32) -> Unmanaged<vImageCVImageFormat>!](vimagecvimageformat_create(_:_:_:_:_:).md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconstcvimageformat)*