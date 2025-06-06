# imageURL(for:)

**Framework**: TV Services  
**Kind**: method

Returns an image associated with the current item.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func imageURL(for traits: TVTopShelfItem.ImageTraits) -> URL?
```

#### Return Value

The image associated with the specified traits; otherwise, `nil` if you did not previously assign an image with the specified traits.

## Parameters

- `traits`: The traits that describe the image.

## See Also

- [func setImageURL(URL?, for: TVTopShelfItem.ImageTraits)](tvtopshelfitem/setimageurl(_:for:).md)
  Associates an image with the current item.
- [TVTopShelfItem.ImageTraits](tvtopshelfitem/imagetraits.md)
  Constants describing the image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/imageurl(for:))*