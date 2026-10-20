# imageSize(for:)

**Framework**: TV Services  
**Kind**: method  
**Role**: Type Method

Returns the dimensions to use for images of the specified shape.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class func imageSize(for shape: TVTopShelfSectionedItem.ImageShape) -> CGSize
```

```objc
+ (CGSize) imageSizeForImageShape:(TVTopShelfSectionedItemImageShape) shape;
```

#### Return Value

The recommended size of the image, in points.

## Parameters

- `shape`: The image shape whose dimensions you want.

## See Also

### Getting the Image Size Information
- [TVTopShelfSectionedItem.ImageShape](../tvtopshelfsectioneditem/imageshape-swift.enum.md)
  Constants indicating the aspect ratio of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfsectionedcontent/imagesize(for:))*