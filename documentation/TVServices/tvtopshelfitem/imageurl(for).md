# imageURL(for:)

**Framework**: TV Services  
**Kind**: method  
**Role**: Instance Method

Returns an image associated with the current item.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func imageURL(for traits: TVTopShelfItem.ImageTraits) -> URL?
```

```objc
- (NSURL *) imageURLForTraits:(TVTopShelfItemImageTraits) traits;
```

#### Return Value

The image associated with the specified traits; otherwise, `nil` if you did not previously assign an image with the specified traits.

## Parameters

- `traits`: The traits that describe the image.

## See Also

### Providing an Image for the Item
- [func setImageURL(URL?, for: TVTopShelfItem.ImageTraits)](./setimageurl%28_,for%29.md)
  Associates an image with the current item.
- [TVTopShelfItem.ImageTraits](./imagetraits.md)
  Constants describing the image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/imageurl(for:))*