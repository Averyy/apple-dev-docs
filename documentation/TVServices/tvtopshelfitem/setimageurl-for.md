# setImageURL(_:for:)

**Framework**: TV Services  
**Kind**: method

Associates an image with the current item.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func setImageURL(_ imageURL: URL?, for traits: TVTopShelfItem.ImageTraits)
```

#### Discussion

Use this method to assign images to a top shelf item. For most items, the system displays only an image. For carousel items, the system initially displays an image, but switches to the preview video when the navigation focus stops on the item.

The system always chooses the image whose traits match the target device.

## Parameters

- `imageURL`: The URL of the image. Specify   to remove the image with the specified traits from the item.
- `traits`: The traits that describe the image.

## See Also

- [func imageURL(for: TVTopShelfItem.ImageTraits) -> URL?](tvtopshelfitem/imageurl(for:).md)
  Returns an image associated with the current item.
- [TVTopShelfItem.ImageTraits](tvtopshelfitem/imagetraits.md)
  Constants describing the image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/setimageurl(_:for:))*