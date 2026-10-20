# vImageConstCVImageFormat

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

An immutable description of image encoding in a Core Video pixel buffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class vImageConstCVImageFormat
```

```c
typedef const struct vImageCVImageFormat * vImageConstCVImageFormatRef;
```

#### Discussion

Use [`vImageCVImageFormat_Copy(_:)`](./vimagecvimageformat_copy%28_%29.md) to create a mutable copy of a [`vImageConstCVImageFormat`](./vimageconstcvimageformat.md) instance.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Creating Core Video image formats
- [class vImageCVImageFormat](./vimagecvimageformat.md)
  A mutable description of image encoding in a Core Video pixel buffer.
- [func vImageCVImageFormat_CreateWithCVPixelBuffer(CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!](./vimagecvimageformat_createwithcvpixelbuffer%28_%29.md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [func vImageCVImageFormat_Create(UInt32, UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, CFString!, CGColorSpace!, Int32) -> Unmanaged<vImageCVImageFormat>!](./vimagecvimageformat_create%28_,_,_,_,_%29.md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconstcvimageformat)*