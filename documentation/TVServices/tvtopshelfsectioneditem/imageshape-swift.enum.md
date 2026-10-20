# TVTopShelfSectionedItem.ImageShape

**Framework**: TV Services  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the aspect ratio of an image.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
enum ImageShape
```

```c
enum TVTopShelfSectionedItemImageShape : NSInteger;
```

## Topics

### Image Shapes
- [TVTopShelfSectionedItem.ImageShape.square](./imageshape-swift.enum/square.md)
  An image with a 1:1 aspect ratio.
- [TVTopShelfSectionedItem.ImageShape.poster](./imageshape-swift.enum/poster.md)
  A poster-shaped image with a 2:3 aspect ratio.
- [TVTopShelfSectionedItem.ImageShape.hdtv](./imageshape-swift.enum/hdtv.md)
  An image with a 16:9 aspect ratio.
### Initializers
- [init?(rawValue: Int)](./imageshape-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Image Size Information
- [class func imageSize(for: TVTopShelfSectionedItem.ImageShape) -> CGSize](../tvtopshelfsectionedcontent/imagesize%28for%29.md)
  Returns the dimensions to use for images of the specified shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfsectioneditem/imageshape-swift.enum)*